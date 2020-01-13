from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Image(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=20)
    description = models.CharField(default="N/A", max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image_address = models.URLField(max_length=200)
    whitelist = models.URLField(default="not provided", null=True, blank=True)

    class Meta:
        db_table = 'Image'
        ordering = ["description", "file_name", "date_posted", "whitelist"]

    def __str__(self):
        return self.file_name

class Flagged(models.Model):
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=150)
    url = models.URLField()
    # def __str__(self):
    #     return self.name