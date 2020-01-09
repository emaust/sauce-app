from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Users(models.Model):
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    social_media = models.CharField(max_length=400, null=True, blank=True)

    class Meta:
        ordering = ["username", "name", "email", "social_media"]

    # def __str__(self):
    #     return 

class Image(models.Model):
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
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