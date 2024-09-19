from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import BandListingForm
from .models import BandListing

# Create your views here.

class BandListingList(generic.ListView):
    queryset = BandListing.objects.filter(status=1)
    template_name = 'band_listing/index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_listings'] = context['object_list']  # Rename context variable
        return context

class CreateListingView(LoginRequiredMixin, CreateView):
    model = BandListing
    form_class = BandListingForm
    template_name = 'band_listing/create_listing.html'
    success_url = reverse_lazy('index')  # Redirect to home page on success

    def form_valid(self, form):
        # Set the current user as the creator of the listing
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to create a band listing.')
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)

class BandListingDetail(generic.DetailView):
    model = BandListing
    template_name = 'band_listing/bandlisting_detail.html'
    slug_field = 'slug'  # Ensure that it's looking up by slug
