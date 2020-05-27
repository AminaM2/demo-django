from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories' #otherwise it would be Categorys

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:category-detail", kwargs={"id": self.id})