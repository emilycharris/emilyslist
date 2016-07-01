from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Region(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Category(models.Model):
    name=models.CharField(max_length=25, default=None)
    parent=models.ForeignKey('self', null=True, blank=True, related_name='child')

    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    location = models.ForeignKey(Region)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to="item_photos", null=True, blank=True)
    category=models.ForeignKey(Category)

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "http://www.clker.com/cliparts/f/Z/G/4/h/Q/no-image-available-md.png"


class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    location = models.ForeignKey(Region, default=1)

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender='auth.User')
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        Token.objects.create(user=instance)
