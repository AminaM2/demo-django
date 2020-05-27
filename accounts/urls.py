from django.urls import path, include
from .views import register_view, LoginView
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]