from django.db import models
from accounts.models import Account
from categories.models import Category
from django.urls import reverse

# Create your models here.
class Book(models.Model): #() indicate inheritance
	title				= models.CharField(max_length=120)
	summary 			= models.TextField()
	author				= models.ForeignKey(Account, on_delete=models.CASCADE) # possible values: [CASCADE, PROTECT, SET_NULL, SET_DEFAULT, SET(value)]
	publication_date	= models.DateField()
	create_stamp        = models.DateField(auto_now_add=True)
	categories			= models.ManyToManyField(Category) # ManyToMany relationship with the Category model class
	price				= models.DecimalField(max_digits = 5, decimal_places = 2)
	nb_likes			= models.IntegerField(default=0, editable=False)
	cover_page			= models.ImageField(upload_to='images/books_cover_pages/', null=True, blank=True) #FileField with built-in validations - comes from Pillow

	def __str__(self):
		return self.title # toString method ==> print(obj)

	def get_absolute_url(self):
		return reverse("books:book-detail", kwargs={"id": self.id})

# check other field types here: https://docs.djangoproject.com/fr/3.0/ref/models/fields/
# possible to write custom model fields