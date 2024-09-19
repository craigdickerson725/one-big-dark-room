from . import views
from .views import CreateListingView, EditListingView, DeleteListingView
from django.urls import path

urlpatterns = [
    path('', views.BandListingList.as_view(), name='index'),  # Home page, list view
    path('create/', CreateListingView.as_view(), name='create_listing'),  # Create a new listing
    path('<slug:slug>/', views.BandListingDetail.as_view(), name='bandlisting_detail'),  # Band detail view
    path('<slug:slug>/edit/', EditListingView.as_view(), name='edit_listing'),  # Edit a listing
    path('<slug:slug>/delete/', DeleteListingView.as_view(), name='delete_listing'),  # Delete a listing
]
