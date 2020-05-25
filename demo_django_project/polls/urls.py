from django.urls import path
from .views import PollListView, PollDetailView, PollCreateView

urlpatterns = [
    path('', PollListView.as_view(), name='poll-list'), # path(route, view, kwargs, name)
    path('<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('create/', PollCreateView.as_view(), name='poll-create'),
]