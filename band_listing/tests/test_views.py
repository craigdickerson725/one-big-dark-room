from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import BandListing, Message

User = get_user_model()

class BandListingViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a band listing for testing
        self.band_listing = BandListing.objects.create(
            band_name='Test Band',
            slug='test-band',
            description='A test band description.',
            created_by=self.user,
            status=1
        )

    def test_band_listing_list_view(self):
        response = self.client.get(reverse('index'))  # Assuming the name of the list view URL is 'index'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band_listing/index.html')
        self.assertContains(response, 'Test Band')

    def test_create_listing_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_listing'), {
            'band_name': 'New Band',
            'slug': 'new-band',
            'description': 'Description for new band.',
            'status': 1
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(BandListing.objects.filter(band_name='New Band').exists())

    def test_band_listing_detail_view(self):
        response = self.client.get(reverse('bandlisting_detail', kwargs={'slug': self.band_listing.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band_listing/bandlisting_detail.html')
        self.assertContains(response, 'Test Band')

    def test_edit_listing_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('edit_listing', kwargs={'slug': self.band_listing.slug}), {
            'band_name': 'Updated Band',
            'slug': 'updated-band',
            'description': 'Updated description.',
            'status': 1
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful edit
        self.band_listing.refresh_from_db()
        self.assertEqual(self.band_listing.band_name, 'Updated Band')

    def test_delete_listing_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('delete_listing', kwargs={'slug': self.band_listing.slug}))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful deletion
        self.assertFalse(BandListing.objects.filter(pk=self.band_listing.pk).exists())

    def test_send_message_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('send_message', kwargs={'slug': self.band_listing.slug}), {
            'message_body': 'Hello!',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful send
        self.assertTrue(Message.objects.filter(message_body='Hello!').exists())

    def test_messages_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('messages'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band_listing/messages.html')

    def test_message_detail_view(self):
        self.client.login(username='testuser', password='password')
        message = Message.objects.create(
            sender=self.user,
            recipient=self.user,
            band_listing=self.band_listing,
            message_body='Test message.'
        )
        response = self.client.get(reverse('message_detail', kwargs={'pk': message.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'band_listing/message_detail.html')
        self.assertContains(response, 'Test message.')
