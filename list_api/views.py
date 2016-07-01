from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import json
from classifieds.models import Listing, Category
from list_api.serializers import ListingSerializer, CategorySerializer


# Create your views here.

class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

class CategoryListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk')
        return Listing.objects.filter(category=category_id)


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.exclude(parent=None)
    serializer_class = CategorySerializer

class SubcategoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.exclude(parent=None)
    serializer_class = CategorySerializer

class SubcategoryListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        subcategory_id = self.kwargs.get('pk')
        return Listing.objects.filter(category=subcategory_id)
