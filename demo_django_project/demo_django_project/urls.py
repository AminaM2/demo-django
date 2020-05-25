"""demo_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('pages.urls')),
	path('categories/', include('categories.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('comments.urls')),
 	path('books/', include('books.urls')),
    path('polls/', include('polls.urls')),
    # Possible to define your URL patterns with regular expressions. To do so, use re_path() instead of path().
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# (a, b, c) = tuple in python = collection of values = immutable (no deletion or reassignation of certain elements in a tuple, only of the tuple as a whole)
# [] = list in python = collection of values = mutable
# {} = dictionary in python = like a set of key: value pairs

# you can leave a trailing comma on the last entry of any python data structure (list, tuple, dictionary)