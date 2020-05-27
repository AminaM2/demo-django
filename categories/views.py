from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Category
from .forms import CategoryForm

from django.views.generic import (
	CreateView,
	UpdateView,
	DetailView,
	DeleteView,
	ListView
)

class CategoryListView(ListView):
	template_name = 'categories/category_list.html'
	queryset = Category.objects.all()

class CategoryDetailView(DetailView):
	template_name = 'categories/category_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Category, id=id_)

class CategoryCreateView(CreateView):
	template_name = 'categories/category_create.html'
	form_class = CategoryForm
	queryset = Category.objects.all()

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('categories:category-list')

class CategoryUpdateView(UpdateView):
	template_name = 'categories/category_create.html'
	form_class = CategoryForm
	queryset = Category.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Category, id=id_)

class CategoryDeleteView(DeleteView):
	template_name = 'categories/category_delete.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Category, id=id_)

	def get_success_url(self):
		return reverse('categories:category-list')
