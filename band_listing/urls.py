from . import views
from .views import (
    CreateListingView,
    EditListingView,
    DeleteListingView,
    SendMessageView,
    InboxView,
    SentMessagesView,
    MessageDetailView
)
from django.urls import path

urlpatterns = [
    path('', views.BandListingList.as_view(), name='index'),  # Home page, list view
    path('create/', CreateListingView.as_view(), name='create_listing'),  # Create a new listing

    # Messaging functionality
    path('inbox/', InboxView.as_view(), name='inbox'),  # View user's inbox
    path('sent/', SentMessagesView.as_view(), name='sent_messages'),  # View user's sent messages (outbox)
    path('inbox/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # View and reply to a message
    path('sent/<int:pk>/', MessageDetailView.as_view(), name='sent_message_detail'),  # Optional: view detail for sent messages

    path('<slug:slug>/', views.BandListingDetail.as_view(), name='bandlisting_detail'),  # Band detail view
    path('<slug:slug>/edit/', EditListingView.as_view(), name='edit_listing'),  # Edit a listing
    path('<slug:slug>/delete/', DeleteListingView.as_view(), name='delete_listing'),  # Delete a listing
    path('<slug:slug>/message/', SendMessageView.as_view(), name='send_message'),  # Send message
]
