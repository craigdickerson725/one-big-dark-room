from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import BandListingForm, MessageForm
from .models import BandListing, Message

# View for displaying the list of band listings
class BandListingList(generic.ListView):
    queryset = BandListing.objects.filter(status=1)  # Show only 'Published' listings
    template_name = 'band_listing/index.html'
    paginate_by = 6  # Pagination, 6 listings per page

    def get_context_data(self, **kwargs):
        # Add additional context data: 'band_listings' will refer to the list of objects
        context = super().get_context_data(**kwargs)
        context['band_listings'] = context['object_list']
        return context

# View for creating a new band listing
class CreateListingView(LoginRequiredMixin, CreateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/create_listing.html'
    success_url = reverse_lazy('index')  # Redirect to index page after successful creation

    def form_valid(self, form):
        # Automatically set the creator and status of the band listing
        form.instance.created_by = self.request.user
        form.instance.status = 1  # Automatically set status to "Published"
        messages.success(self.request, 'Band listing successfully created!')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Ensure the user is authenticated before allowing them to create a listing
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to create a band listing.')
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)

# View for displaying details of a single band listing
class BandListingDetail(generic.DetailView):
    model = BandListing
    template_name = 'band_listing/bandlisting_detail.html'
    slug_field = 'slug'  # Use 'slug' field for finding the object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        band_listing = self.get_object()

        # Check if the band listing has a photo, otherwise use a default image
        if not band_listing.photo:
            context['default_photo'] = 'images/default-image.jpg'  # Default image path
        else:
            context['default_photo'] = band_listing.photo.url

        return context

# View for editing an existing band listing
class EditListingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/edit_listing.html'
    success_url = reverse_lazy('index')  # Redirect to index page after successful editing

    def form_valid(self, form):
        # Ensure the listing is updated by the user who created it
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Band listing successfully edited!')
        return super().form_valid(form)

    def test_func(self):
        # Check if the logged-in user is the creator of the listing
        listing = self.get_object()
        return self.request.user == listing.created_by

# View for deleting a band listing
class DeleteListingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BandListing
    success_url = reverse_lazy('index')  # Redirect to index page after deletion

    def test_func(self):
        # Check if the logged-in user is the creator of the listing
        listing = self.get_object()
        return self.request.user == listing.created_by

    def post(self, request, *args, **kwargs):
        # Confirm deletion with a success message
        messages.success(self.request, 'Band listing successfully deleted.')
        return super().post(request, *args, **kwargs)

# View for sending messages to the creator of a band listing
class SendMessageView(LoginRequiredMixin, FormView):
    form_class = MessageForm
    template_name = 'band_listing/send_message.html'

    def form_valid(self, form):
        # Send a message to the creator of the band listing
        band_listing = get_object_or_404(BandListing, slug=self.kwargs['slug'])
        recipient = band_listing.created_by
        form.instance.sender = self.request.user
        form.instance.recipient = recipient
        form.instance.band_listing = band_listing
        form.save()
        messages.success(self.request, 'Message sent successfully.')
        return redirect('bandlisting_detail', slug=band_listing.slug)

    def get_context_data(self, **kwargs):
        # Include the band listing in the context
        context = super().get_context_data(**kwargs)
        context['band_listing'] = get_object_or_404(BandListing, slug=self.kwargs['slug'])
        return context

# View for showing both inbox and outbox messages for the user
class MessagesView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'band_listing/messages.html'

    def get_context_data(self, **kwargs):
        # Separate the inbox and outbox messages
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['inbox_messages'] = Message.objects.filter(recipient=user, deleted_by_recipient=False).order_by('-timestamp')
        context['outbox_messages'] = Message.objects.filter(sender=user, deleted_by_sender=False).order_by('-timestamp')
        # Add a count of unread messages for the inbox alert
        context['unread_count'] = Message.objects.filter(recipient=user, is_read=False).count()
        return context

# View for reading and replying to a specific message
class MessageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Message
    template_name = 'band_listing/message_detail.html'
    context_object_name = 'original_message'

    def get_context_data(self, **kwargs):
        # Mark message as read and provide a form for replying
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        message = self.get_object()
        if not message.is_read:
            message.is_read = True
            message.save()
        return context

    def post(self, request, *args, **kwargs):
        # Handle sending a reply to the original message
        self.object = self.get_object()
        form = MessageForm(request.POST)
        if form.is_valid():
            reply_message = form.save(commit=False)
            reply_message.sender = self.request.user
            reply_message.recipient = self.object.sender
            reply_message.band_listing = self.object.band_listing
            reply_message.save()
            messages.success(request, 'Reply sent successfully.')
            return redirect('messages')
        messages.error(request, 'There was an error sending your reply.')
        return self.render_to_response({'form': form, 'original_message': self.object})

# Function for allowing a sender to delete a message
def delete_by_sender(request, id):
    message = get_object_or_404(Message, id=id)
    if not message.sender == request.user:
        messages.error(request, "You cannot delete this message.")
        return redirect('messages')
    if message.deleted_by_recipient:
        message.delete()
        messages.success(request, "Message deleted successfully.")
        return redirect('messages')
    else:
        message.deleted_by_sender = True
        message.save()
        messages.success(request, "Message deleted successfully.")
        return redirect('messages')

# Function for allowing a recipient to delete a message
def delete_by_recipient(request, id):
    message = get_object_or_404(Message, id=id)
    if not message.recipient == request.user:
        messages.error(request, "You cannot delete this message.")
        return redirect('messages')
    if message.deleted_by_sender:
        message.delete()
        messages.success(request, "Message deleted successfully.")
        return redirect('messages')
    else:
        message.deleted_by_recipient = True
        message.save()
        messages.success(request, "Message deleted successfully.")
        return redirect('messages')
