from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import BandListing

# Create your views here.
# def my_band_listing(request):
#     return HttpResponse("Hello, Dark Room!")
class BandListingList(generic.ListView):
    # model = BandListing
    queryset = BandListing.objects.filter(status=1)
    template_name = 'band_listing/bandlisting_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['band_listings'] = context['object_list']  # Rename context variable
        return context

class BandListingDetail(generic.DetailView):
    model = BandListing
    template_name = 'band_listing/bandlisting_detail.html'