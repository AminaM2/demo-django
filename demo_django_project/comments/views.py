from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Comment
from .forms import CommentForm
from books.models import Book

from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView
)

class CommentListView(ListView):
    template_name = 'comments/comment_list.html'
    queryset = Comment.objects.all()

class CommentDetailView(DetailView):
    template_name = 'comments/comment_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Comment, id=id_)

class CommentCreateView(CreateView):
    template_name = 'comments/comment_create.html'
    form_class = CommentForm
    queryset = Comment.objects.all()

    def get_success_url(self):
        return reverse('books:book-list') #detail book

    def form_valid(self, form):
        form.instance.author = self.request.user #reference the currently logged in user
        book_id = self.kwargs.get('book_id', None) #pass additionnal parameters / get them with kwargs
        form.instance.book = Book.objects.get(id=book_id)
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    template_name = 'comments/comment_create.html'
    form_class = CommentForm
    queryset = Comment.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Comment, id=id_)

class CommentDeleteView(DeleteView):
    template_name = 'comments/comment_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Comment, id=id_)

    def get_success_url(self):
        return reverse('comments:comment-list')
