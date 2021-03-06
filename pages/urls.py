from django.contrib import admin
from django.urls import path, include

from pages.views import index_view, contact_view, about_view

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about')
]