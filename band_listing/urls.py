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
    # Home page, list view
    path('', views.BandListingList.as_view(), name='index'),
    # Create a new listing
    path('create/', CreateListingView.as_view(), name='create_listing'),

    # Messaging functionality
    # View all user's messages (received and sent)
    path('messages/', MessagesView.as_view(), name='messages'),
    # View and reply to a message
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),  # noqa
    path('messages/<int:id>/delete/sender/', views.delete_by_sender, name='delete_message_sender'),  # noqa
    path('messages/<int:id>/delete/recipient/', views.delete_by_recipient, name='delete_message_recipient'),  # noqa
    # Band detail view
    path('<slug:slug>/', views.BandListingDetail.as_view(), name='bandlisting_detail'),  # noqa
    # Edit a listing
    path('<slug:slug>/edit/', EditListingView.as_view(), name='edit_listing'),
    # Delete a listing
    path('<slug:slug>/delete/', DeleteListingView.as_view(), name='delete_listing'),  # noqa
    # Send message
    path('<slug:slug>/message/', SendMessageView.as_view(), name='send_message'),  # noqa
]
