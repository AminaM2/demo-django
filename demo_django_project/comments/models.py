from django.db import models
from accounts.models import Account
from books.models import Book
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
    title               = models.CharField(max_length=120) # max_length is mandatory with a CharField
    content             = models.TextField()
    author              = models.ForeignKey(Account, on_delete=models.CASCADE)
    anonymous           = models.BooleanField(default=False)
    book                = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_stamp        = models.DateField(auto_now_add=True) # only when first created 
    last_update_stamp   = models.DateField(auto_now=True) # every time save() method is called, including when it is first created

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("comments:comment-detail", kwargs={"id": self.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)