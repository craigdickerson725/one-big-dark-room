# Generated by Django 4.2.16 on 2024-09-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_listing', '0004_alter_bandlisting_options_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandlisting',
            name='photo',
            field=models.ImageField(default='default-image.jpg', upload_to='band_photos/'),
        ),
    ]
