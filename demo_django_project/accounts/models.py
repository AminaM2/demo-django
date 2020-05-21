from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    is_author	= models.BooleanField(default=False)
    is_visitor	= models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def has_author_account(self):
        return self.is_author