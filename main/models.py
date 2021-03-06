from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=15, null=True, blank=True)
    youtube = models.CharField(max_length=70, null=True, blank=True)
    website = models.URLField(max_length=50, null=True, blank=True)
    patreon = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    file_name = models.CharField(max_length=20)
    description = models.CharField(default="N/A", max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image_address = models.URLField(max_length=200)
    results = ArrayField(models.CharField(max_length=300, blank=True), null=True, blank=True, default=list)
    reported = ArrayField(models.CharField(max_length=300, blank=True), null=True, blank=True, default=list)

    class Meta:
        db_table = 'Image'
        ordering = ["description", "file_name", "date_posted"]

    def __str__(self):
        return self.file_name


class HighRisk(models.Model):
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=150)
    url = models.URLField()
    # def __str__(self):
    #     return self.name