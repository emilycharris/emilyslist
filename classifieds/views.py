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

class CategoryDetailView(DetailView):
    model = Category

class ListingCreateView(CreateView):
    pass

class ListingListView(ListView):
    pass

class ListingDetailView(DetailView):
    pass

class ProfileUpdateView(UpdateView):
    pass

class ListingDeleteView(DeleteView):
    pass

class ListingUpdateView(UpdateView):
    pass
