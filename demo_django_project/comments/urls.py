from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

app_name = 'comments'

urlpatterns = [
    path('', CommentListView.as_view(), name='comment-list'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'), #show pk vs. id
    path('<int:book_id>/create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete')
]