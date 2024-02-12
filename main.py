# models.py

from django.db import models

class Asset(models.Model):
    asset_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    # Add other fields as needed

class VandalismRecord(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    time = models.TimeField()
    before_photo = models.ImageField(upload_to='vandalism_photos/before/', blank=True, null=True)
    after_photo = models.ImageField(upload_to='vandalism_photos/after/', blank=True, null=True)
    # Add other fields as needed
