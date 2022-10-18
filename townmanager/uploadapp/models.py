from django.db import models

class Upload(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.FileField(blank=True, upload_to="photo_%Y_%m_%d")