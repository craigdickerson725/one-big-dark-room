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

# Band listing list view
class BandListingList(generic.ListView):
    queryset = BandListing.objects.filter(status=1)
    template_name = 'band_listing/index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_listings'] = context['object_list']
        return context

# Create listing view
class CreateListingView(LoginRequiredMixin, CreateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/create_listing.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.status = 1  # Automatically set to "Published"
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to create a band listing.')
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)

# Band listing detail view
class BandListingDetail(generic.DetailView):
    model = BandListing
    template_name = 'band_listing/bandlisting_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        band_listing = self.get_object()

        # Check if the band listing has a photo, else provide a default image
        if not band_listing.photo:
            context['default_photo'] = 'images/default-image.jpg'  # Update with your default image path in the static directory
        else:
            context['default_photo'] = band_listing.photo.url

        return context

# Edit band listing view
class EditListingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/edit_listing.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.created_by

# Delete band listing view
class DeleteListingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BandListing
    template_name = 'band_listing/confirm_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.created_by

# Send message view
class SendMessageView(LoginRequiredMixin, FormView):
    form_class = MessageForm
    template_name = 'band_listing/send_message.html'

    def form_valid(self, form):
        band_listing = get_object_or_404(BandListing, slug=self.kwargs['slug'])
        recipient = band_listing.created_by
        form.instance.sender = self.request.user
        form.instance.recipient = recipient
        form.instance.band_listing = band_listing
        form.save()
        messages.success(self.request, 'Message sent successfully.')
        return redirect('bandlisting_detail', slug=band_listing.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_listing'] = get_object_or_404(BandListing, slug=self.kwargs['slug'])
        return context

# User's messages view (inbox and outbox)
class MessagesView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'band_listing/messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Separate inbox and outbox messages
        context['inbox_messages'] = Message.objects.filter(recipient=user).order_by('-timestamp')
        context['outbox_messages'] = Message.objects.filter(sender=user).order_by('-timestamp')
        # Count unread messages for the navbar alert
        context['unread_count'] = Message.objects.filter(recipient=user, is_read=False).count()
        return context

# Message detail view (to read and reply)
class MessageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Message
    template_name = 'band_listing/message_detail.html'
    context_object_name = 'original_message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        message = self.get_object()
        if not message.is_read:
            message.is_read = True
            message.save()
        return context

    def post(self, request, *args, **kwargs):
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

# Delete message view
class DeleteMessageView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'band_listing/confirm_delete_message.html'
    success_url = reverse_lazy('messages')

    def get_object(self, queryset=None):
        message = super().get_object(queryset)
        if message.recipient != self.request.user and message.sender != self.request.user:
            messages.error(self.request, "You cannot delete this message.")
            return None
        return message

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj:
            messages.success(request, "Message deleted successfully.")
            return super().delete(request, *args, **kwargs)
        return HttpResponseRedirect(self.success_url)
