# Generated by Django 5.1.6 on 2025-02-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age_range',
            field=models.CharField(blank=True, choices=[('18-25', '18-25'), ('25-30', '25-30'), ('30-35', '30-35'), ('35-40', '35-40'), ('40-45', '40-45'), ('45-50', '45-50'), ('50+', '50+')], max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('O', 'Other')], max_length=2),
        ),
    ]
