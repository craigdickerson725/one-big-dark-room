from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandListingList.as_view(), name='home'),
    path('<slug:slug>/', views.BandListingDetail.as_view(), name='band_listing_detail'),
]