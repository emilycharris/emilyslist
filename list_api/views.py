from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import json
from classifieds.models import Listing, Category
from list_api.serializers import ListingSerializer, CategorySerializer
from list_api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User



# Create your views here.

class ListingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

class CategoryListingListAPIView(generics.ListAPIView):
    model = Listing
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk')
        return Listing.objects.filter(category__parent=category_id)


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.exclude(parent=None)
    serializer_class = CategorySerializer

class SubcategoryRetrieveUpdateAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.exclude(parent=None)
    serializer_class = CategorySerializer

class SubcategoryListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        subcategory_id = self.kwargs.get('pk')
        return Listing.objects.filter(category=subcategory_id)
