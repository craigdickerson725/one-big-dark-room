from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Choices for the status of a band listing
STATUS = ((0, "Draft"), (1, "Published"))


# Model for band listings
class BandListing(models.Model):
    band_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Cloudinary field for the band photo, with a default placeholder image
    photo = CloudinaryField(
        'photo', default='default-image_kfzhkf.jpg', blank=True, null=True)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_listings")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=1)  # Default set to 'Published'
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

    @property
    def photo_url(self):
        # If photo is uploaded, return the Cloudinary URL,
        # otherwise return the default static image URL
        if self.photo:
            return self.photo.url
        return '/static/images/default-image.jpg'


# Model for messages between users regarding band listings
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)  # noqa
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)  # noqa
    band_listing = models.ForeignKey(BandListing, related_name='messages', on_delete=models.CASCADE)  # noqa
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Field to track if the message has been read
    is_read = models.BooleanField(default=False)
    deleted_by_sender = models.BooleanField(default=False)
    deleted_by_recipient = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        snippet = self.message_body[:50] + '...' if len(
            self.message_body) > 50 else self.message_body
        return f"Message from {self.sender.username} to {self.recipient.username}: {snippet}"  # noqa
