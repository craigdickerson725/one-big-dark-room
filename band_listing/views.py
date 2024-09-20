from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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
        recipient = band_listing.created_by  # Send message to the creator of the band listing
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

# User's inbox view
class InboxView(LoginRequiredMixin, generic.ListView):
    template_name = 'band_listing/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Count unread messages
        context['unread_count'] = Message.objects.filter(recipient=self.request.user, is_read=False).count()
        return context

# User's sent messages view
class SentMessagesView(LoginRequiredMixin, generic.ListView):
    template_name = 'band_listing/sent_messages.html'
    context_object_name = 'sent_messages'

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user).order_by('-timestamp')

# Message detail view (to read and reply)
class MessageDetailView(LoginRequiredMixin, generic.DetailView, FormView):
    model = Message
    template_name = 'band_listing/message_detail.html'
    form_class = MessageForm

    def form_valid(self, form):
        # Reply logic
        original_message = self.get_object()
        reply_message = form.save(commit=False)
        reply_message.sender = self.request.user
        reply_message.recipient = original_message.sender
        reply_message.band_listing = original_message.band_listing
        reply_message.save()
        messages.success(self.request, 'Reply sent successfully.')
        return redirect('inbox')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['original_message'] = self.get_object()
        # Mark the message as read
        message = self.get_object()
        message.is_read = True  # Set is_read to True
        message.save()  # Save the updated message
        return context
