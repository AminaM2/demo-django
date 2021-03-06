from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm
from comments.forms import CommentForm
from django.http import HttpResponseRedirect

from django.views.generic import (
	CreateView,
	UpdateView,
	DetailView,
	DeleteView,
	ListView
)

class BookListView(ListView):
	template_name = 'books/book_list.html'
	model = Book

class BookDetailView(DetailView):
	template_name = 'books/book_detail.html'
	
	def get_object(self): #if you use a parameter name different from pk
		id_ = self.kwargs.get("id")
		return get_object_or_404(Book, id=id_)

	def get_context_data(self, **kwargs): #specify additionnal context variables
		context = super().get_context_data(**kwargs)
		context['comment_form'] = CommentForm
		context['comment_list'] = Book.objects.get(id=self.kwargs.get("id")).comment_set.all()
		return context

class BookCreateView(CreateView):
	template_name = 'books/book_create.html'
	form_class = BookForm
	queryset = Book.objects.all() # or model = Book

	def form_valid(self, form):
		form.instance.author = self.request.user #reference the currently logged in user
		return super().form_valid(form)

class BookUpdateView(UpdateView):
	template_name = 'books/book_create.html'
	form_class = BookForm
	model = Book

class BookDeleteView(DeleteView):
	template_name = 'books/book_delete.html'
	model = Book

	def get_success_url(self):
		return reverse('books:book-list')

def like_view(request, pk):
	book = get_object_or_404(Book, pk=pk)
	book.like()
	return HttpResponseRedirect(reverse('books:book-detail', args=[pk]))