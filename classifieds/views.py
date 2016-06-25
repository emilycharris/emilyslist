from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from classifieds.models import Category, Listing, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.urlresolvers import reverse_lazy

from classifieds.models import Region, Profile, Category, Listing


# Create your views here.

class IndexView(ListView):
    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        return Category.objects.filter(parent=None)

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"

class CategoryListView(ListView):
    model = Listing
    template_name = 'classifieds/category_list.html'

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk') # none needed as second argument???
        return Listing.objects.filter(category=category_id)

class ListingCreateView(CreateView):
    model = Listing
    fields = ["title", 'price', 'location', 'body', 'photo', 'category']
    success_url = reverse_lazy("index_view")

class ListingDetailView(DetailView):
    pass

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['location']
    success_url = reverse_lazy('index_view')

    def get_object(self, queryset=None):
        return self.request.user.profile

class ListingDeleteView(DeleteView):
    pass

class ListingUpdateView(UpdateView):
    pass

class CityListingView(ListView):
    model = Listing

    def get_queryset(self, **kwargs):
        city_id = self.kwargs.get('pk')
        return Listing.objects.filter(location=city_id)

class RegionListView(ListView):
    model = Region
