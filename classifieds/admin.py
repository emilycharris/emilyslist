from django.contrib import admin
from classifieds.models import Region, Listing, Profile, Category


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "location", "body", "photo", "category"]
    search_fields = ["body"]

admin.site.register(Listing)

class RegionAdmin(admin.ModelAdmin):
    list_display = ["location"]

admin.site.register(Region)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["location"]

admin.site.register(Profile)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Category)
