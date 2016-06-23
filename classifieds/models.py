from django.db import models

# Create your models here.

class Region(models.Model):
    location = models.CharField(max_length=50)


class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    location = models.ForeignKey(Region)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to="profile_photos", null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    location = models.ForeignKey(Region)
