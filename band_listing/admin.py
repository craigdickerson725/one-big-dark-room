from django.contrib import admin
from .models import BandListing, Message
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BandListing)
class BandListingAdmin(SummernoteModelAdmin):
    list_display = ('band_name', 'slug', 'status', 'created_at')
    search_fields = ['band_name', 'description']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('band_name',)}
    summernote_fields = ('description',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Display relevant fields
    list_display = ('sender', 'recipient', 'band_listing', 'timestamp')
    # Add search fields
    search_fields = ['sender__username', 'recipient__username', 'message_body']
    list_filter = ('timestamp',)  # Filter messages by timestamp
    ordering = ('-timestamp',)  # Order messages by timestamp descending

    def recipient_username(self, obj):
        return obj.recipient.username if obj.recipient else 'Unknown'  # noqa
    # Allows sorting by recipient
    recipient_username.admin_order_field = 'recipient'
    recipient_username.short_description = 'Recipient Username'
