from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandListingList.as_view(), name='index'),  # Home page, list view
    path('create/', views.CreateListingView.as_view(), name='create_listing'),  # Create a new listing
    path('<slug:slug>/', views.BandListingDetail.as_view(), name='bandlisting_detail'),  # Band detail view
]