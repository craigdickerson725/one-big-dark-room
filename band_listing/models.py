from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

class BandListing(models.Model):
    band_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    photo = models.ImageField(upload_to='band_photos/', default='default-image.jpg')
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)  # Default set to 'Published'
    snippet = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.band_name} | {self.created_by.username}"

    def save(self, *args, **kwargs):
        # Automatically generate slug from band name if not provided
        if not self.slug:
            self.slug = slugify(self.band_name)
        super().save(*args, **kwargs)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    band_listing = models.ForeignKey(BandListing, related_name='messages', on_delete=models.CASCADE)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Field to track if the message has been read

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        snippet = self.message_body[:50] + '...' if len(self.message_body) > 50 else self.message_body
        return f"Message from {self.sender.username} to {self.recipient.username}: {snippet}"
