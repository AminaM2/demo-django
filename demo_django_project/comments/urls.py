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
    path('<int:id>/', CommentDetailView.as_view(), name='comment-detail'), #show pk vs. id
    path('<int:book_id>/create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:id>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:id>/delete/', CommentDeleteView.as_view(), name='comment-delete')
]