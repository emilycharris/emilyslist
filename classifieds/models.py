from django.db import models

# Create your models here.

class Region(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Category(models.Model):
    name=models.CharField(max_length=25, default=None)
    subcategory=models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    location = models.ForeignKey(Region)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to="profile_photos", null=True, blank=True)
    category=models.ForeignKey(Category)

class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    location = models.ForeignKey(Region)
