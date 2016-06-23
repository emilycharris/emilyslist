from django.contrib import admin
from classifieds.models import Region, Listing, Profile


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "location", "body", "photo"]
    search_fields = ["body"]

admin.site.register(Listing, ListingAdmin)

admin.site.register(Region)

admin.site.register(Profile)
