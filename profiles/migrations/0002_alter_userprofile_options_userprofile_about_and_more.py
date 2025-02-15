# Generated by Django 5.1.6 on 2025-02-15 11:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='font_family',
            field=models.CharField(choices=[('default', 'Default'), ('serif', 'Serif'), ('sans-serif', 'Sans-serif'), ('dyslexie', 'Dyslexie')], default='default', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('O', 'Other')], max_length=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Profile Image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sexual_orientation',
            field=models.CharField(blank=True, choices=[('H', 'Heterosexual'), ('G', 'Gay'), ('L', 'Lesbian'), ('B', 'Bisexual'), ('A', 'Asexual'), ('P', 'Pansexual'), ('Q', 'Queer'), ('O', 'Other')], max_length=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=5),
        ),
    ]
