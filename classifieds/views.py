from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from classifieds.models import Category, Listing, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

class CategoryListThumbnailView(ListView):
    model = Listing
    template_name = 'classifieds/category_list_thumbnail.html'

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(category=category_id).order_by(sort)
        else:
            return Listing.objects.filter(category=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('pk')
        return context

class CategoryListGalleryView(ListView):
    model = Listing
    template_name = 'classifieds/category_list_gallery.html'

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(category=category_id).order_by(sort)
        else:
            return Listing.objects.filter(category=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('pk')
        return context

class CategoryListListView(ListView):
    model = Listing
    template_name = 'classifieds/category_list_list.html'

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(category=category_id).order_by(sort)
        else:
            return Listing.objects.filter(category=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('pk')
        return context

class ListingCreateView(CreateView):
    model = Listing
    fields = ["title", 'price', 'location', 'body', 'photo', 'category']
    success_url = reverse_lazy("index_view")

    def get_form(self, form_class):
        form = super(ListingCreateView, self).get_form(form_class)
        category = Category.objects.exclude(parent=None)
        form.fields['category'].queryset = category
        return form

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        return super().form_valid(form)

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'classifieds/listing_detail.html'

    def get_queryset(self, **kwargs):
        listing_id = self.kwargs.get('pk')
        return Listing.objects.filter(id=listing_id)

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['location']
    success_url = reverse_lazy('profile_list_view')

    def get_object(self, queryset=None):
        return self.request.user.profile

class ProfileListView(ListView):
    model = Listing
    template_name = 'classifieds/profile_list_list.html'

    def get_queryset(self, **kwargs):
        return Listing.objects.filter(user=self.request.user)

    def get_queryset(self, **kwargs):
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(user=self.request.user).order_by(sort)
        else:
            return Listing.objects.filter(user=self.request.user)

class ListingUpdateView(UpdateView):
    success_url = reverse_lazy("profile_list_view")
    fields = ["title", 'price', 'location', 'body', 'photo', 'category']

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)

    def get_form(self, form_class):
        form = super(ListingUpdateView, self).get_form(form_class)
        category = Category.objects.exclude(parent=None)
        form.fields['category'].queryset = category
        return form

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        return super().form_valid(form)

class ListingDeleteView(DeleteView):
    success_url = reverse_lazy("profile_list_view")
    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)

class CityListThumbnailView(ListView):
    model = Listing
    template_name = 'classifieds/city_list_thumbnail.html'

    def get_queryset(self, **kwargs):
        city_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(location=city_id).order_by(sort)
        else:
            return Listing.objects.filter(location=city_id)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_id'] = self.kwargs.get('pk')
        return context

class CityListGalleryView(ListView):
    model = Listing
    template_name = 'classifieds/city_list_gallery.html'

    def get_queryset(self, **kwargs):
        city_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(location=city_id).order_by(sort)
        else:
            return Listing.objects.filter(location=city_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_id'] = self.kwargs.get('pk')
        return context

class CityListListView(ListView):
    model = Listing
    template_name = 'classifieds/city_list_list.html'

    def get_queryset(self, **kwargs):
        city_id = self.kwargs.get('pk')
        sort = self.request.GET.get('sort')
        if sort:
            return Listing.objects.filter(location=city_id).order_by(sort)
        else:
            return Listing.objects.filter(location=city_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_id'] = self.kwargs.get('pk')
        return context

class RegionListView(ListView):
    model = Region
