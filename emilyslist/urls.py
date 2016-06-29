"""emilyslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from classifieds.views import (IndexView, ListingCreateView, ListingDetailView,
ProfileUpdateView, ListingDeleteView, CreateUserView,
RegionListView, CityListThumbnailView, CategoryListThumbnailView,
CategoryListGalleryView, CityListGalleryView, CategoryListListView, CityListListView)
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_listing/$', ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url(r'^accounts/profile/$', login_required(ProfileUpdateView.as_view()), name="profile_update_view"),
    url(r'^listing/(?P<pk>\d+)/delete/$', ListingDeleteView.as_view(), name="listing_delete_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^region_list', RegionListView.as_view(), name='region_list_view'),
    url(r'^category/(?P<pk>\d+)/thumbnail/$', CategoryListThumbnailView.as_view(), name='category_list_thumbnail_view'),
    url(r'^city_list/(?P<pk>\w+)/thumbnail/$', CityListThumbnailView.as_view(), name='city_list_thumbnail_view'),
    url(r'^category/(?P<pk>\d+)/gallery/$', CategoryListGalleryView.as_view(), name='category_list_gallery_view'),
    url(r'^city_list/(?P<pk>\w+)/gallery/$', CityListGalleryView.as_view(), name='city_list_gallery_view'),
    url(r'^category/(?P<pk>\d+)/list/$', CategoryListListView.as_view(), name='category_list_list_view'),
    url(r'^city_list/(?P<pk>\w+)/list/$', CityListListView.as_view(), name='city_list_list_view'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
