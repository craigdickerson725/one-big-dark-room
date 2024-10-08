# Generated by Django 4.2.16 on 2024-09-12 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('band_listing', '0002_bandlisting_snippet_bandlisting_updated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('band_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='band_listing.bandlisting')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
