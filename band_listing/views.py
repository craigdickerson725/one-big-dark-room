from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
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

class CreateListingView(CreateView):
    model = BandListing
    fields = ['band_name', 'photo', 'description', 'status']  # Include fields to be filled in
    template_name = 'band_listing/create_listing.html'
    success_url = '/'  # Redirect to home after successful creation

class BandListingDetail(generic.DetailView):
    model = BandListing
    template_name = 'band_listing/bandlisting_detail.html'
    slug_field = 'slug'  # Ensure that it's looking up by slug