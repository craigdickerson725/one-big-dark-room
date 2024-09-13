from django.contrib import admin
from .models import BandListing, Message
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BandListing)
class BandListingAdmin(SummernoteModelAdmin):
    list_display = ('band_name', 'slug', 'status', 'created_at')  # Adjust based on BandListing fields
    search_fields = ['band_name', 'description']  # You can add fields that make sense for searching
    list_filter = ('status', 'created_at')  # Filter by status and creation date
    prepopulated_fields = {'slug': ('band_name',)}  # Automatically generate slug from band_name
    summernote_fields = ('description',)  # Add the field(s) where you want to use Summernote editor

# Register your models here.
# admin.site.register(BandListing)
admin.site.register(Message)
