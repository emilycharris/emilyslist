from rest_framework import serializers
from classifieds.models import Listing, Category

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'user', 'title', 'price', 'location', 'body', 'photo', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']
