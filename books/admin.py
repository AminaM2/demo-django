from django.contrib import admin
from .models import Book # in java: import models.Article

# Register your models here.
admin.site.register(Book)