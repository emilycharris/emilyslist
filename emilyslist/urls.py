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
from classifieds.views import IndexView, ListingCreateView, ListingListView, ListingDetailView, ProfileUpdateView, ListingDeleteView, ListingUpdateView, CreateUserView, CategoryListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_listing/$', ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^list_listing/$', ListingListView.as_view(), name='listing_list_view'),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_update_view"),
    url(r'^listing/(?P<pk>\d+)/delete/$', ListingDeleteView.as_view(), name="listing_delete_view"),
    url(r'^listing/(?P<pk>\d+)/update/$', ListingUpdateView.as_view(), name='listing_update_view'),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^category/(?P<pk>\d+)/$', CategoryListView.as_view(), name='category_list_view')
 ]
