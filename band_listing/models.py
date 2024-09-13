from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class BandListing(models.Model):
    band_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='band_photos/', blank=True, null=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    snippet = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # Order by the most recent 'created_at' timestamp (descending order)
        ordering = ['-created_at']
    
    # String representation of the object, combining the band name and the username of the creator
    def __str__(self):
        return f"{self.band_name} | {self.created_by.username}"


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    band_listing = models.ForeignKey(BandListing, related_name='messages', on_delete=models.CASCADE)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order by most recent 'timestamp' first (descending order)
        ordering = ['-timestamp']
    
    def __str__(self):
        # Return a snippet (first 50 characters) of the message body
        return self.message_body[:50] + '...' if len(self.message_body) > 50 else self.message_body
