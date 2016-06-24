from django.contrib import admin
from classifieds.models import Region, Listing, Profile, Category


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "location", "body", "photo", "category"]
    search_fields = ["body"]

admin.site.register(Listing, ListingAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ["location"]

admin.site.register(Region, RegionAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["location"]

admin.site.register(Profile, ProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

admin.site.register(Category, CategoryAdmin)
