from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Account
from django.contrib.auth import get_user_model
from .forms import AccountForm
from django.contrib.auth.views import LoginView
from .forms import LoginForm

# Create your views here.
def register_view(request):
	User = get_user_model()
	if request.method == 'POST':
		form = AccountForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')

	else:
		form = AccountForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)


class LoginView(LoginView):
    authentication_form = LoginForm #override the default form