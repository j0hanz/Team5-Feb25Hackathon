# Generated by Django 5.1.6 on 2025-02-15 20:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='nobody_nrbk5n', help_text='Upload a profile picture', max_length=255, null=True, verbose_name='image'),
        ),
    ]
