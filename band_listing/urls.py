from . import views
from .views import (
    CreateListingView,
    EditListingView,
    DeleteListingView,
    SendMessageView,
    MessagesView,  
    MessageDetailView,
)
from django.urls import path

urlpatterns = [
    path('', views.BandListingList.as_view(), name='index'),  # Home page, list view
    path('create/', CreateListingView.as_view(), name='create_listing'),  # Create a new listing

    # Messaging functionality
    path('messages/', MessagesView.as_view(), name='messages'),  # View all user's messages (received and sent)
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # View and reply to a message
    path('messages/<int:id>/delete/sender/', views.delete_by_sender, name='delete_message_sender'),
    path('messages/<int:id>/delete/recipient/', views.delete_by_recipient, name='delete_message_recipient'),

    path('<slug:slug>/', views.BandListingDetail.as_view(), name='bandlisting_detail'),  # Band detail view
    path('<slug:slug>/edit/', EditListingView.as_view(), name='edit_listing'),  # Edit a listing
    path('<slug:slug>/delete/', DeleteListingView.as_view(), name='delete_listing'),  # Delete a listing
    path('<slug:slug>/message/', SendMessageView.as_view(), name='send_message'),  # Send message
]
