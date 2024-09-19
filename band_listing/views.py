from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import BandListingForm
from .models import BandListing

# Band listing list view
class BandListingList(generic.ListView):
    queryset = BandListing.objects.filter(status=1)
    template_name = 'band_listing/index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_listings'] = context['object_list']  # Rename context variable
        return context

# Create listing view
class CreateListingView(LoginRequiredMixin, CreateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/create_listing.html'
    success_url = reverse_lazy('index')  # Redirect to home page on success

    def form_valid(self, form):
        # Set the current user as the creator of the listing
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
    slug_field = 'slug'  # Ensure that it's looking up by slug

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
        # Only allow the creator of the listing to edit
        listing = self.get_object()
        return self.request.user == listing.created_by

# Delete band listing view
class DeleteListingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BandListing
    template_name = 'band_listing/confirm_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        # Only allow the creator of the listing to delete
        listing = self.get_object()
        return self.request.user == listing.created_by
