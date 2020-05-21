from django.http import HttpResponse
from django.shortcuts import render, redirect
from books.models import Book

# Create your views here.
def index_view(request):
	if request.user.is_authenticated:
		#show the 3 more liked books
		new_arrivals_list 	= Book.objects.order_by('create_stamp')[:3] #order by ascending order, keep first 3
		top_books_list 		= Book.objects.order_by('-nb_likes')[:3] #order by descending order, keep first 3
		context = {
			'new_arrivals_list'	: new_arrivals_list,
			'top_books_list'	: top_books_list
		}
		return render(request, 'index.html', context)
	else:
		return redirect('accounts:login')

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})