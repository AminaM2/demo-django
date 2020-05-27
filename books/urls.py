from django.urls import path
from .views import (
	BookListView,
	BookDetailView,
	BookCreateView,
	BookUpdateView,
	BookDeleteView,
	like_view
)

app_name = 'books'

urlpatterns = [
	path('', BookListView.as_view(), name='book-list'),
	path('<int:id>/', BookDetailView.as_view(), name='book-detail'),
	path('create/', BookCreateView.as_view(), name='book-create'),
	path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
	path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
	path('<int:pk>/like/', like_view, name='book-like')
]