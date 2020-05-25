from django.db import models
from accounts.models import Account
from books.models import Book
from django.urls import reverse

# Create your models here.
class Poll(models.Model):
    question        = models.TextField()
    poller          = models.ForeignKey(Account, on_delete=models.PROTECT) #prevents referenced object from being deleted
    create_stamp    = models.DateField(auto_now_add=True)
    book            = models.ForeignKey(Book, on_delete=models.PROTECT)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("poll-detail", kwargs={"pk": self.id})

class PollResult(models.Model):

    class Meta:
        verbose_name = 'Poll Result' # otherwise PollResult becomes poll result.
        ordering = ['create_stamp']
        indexes = [
            models.Index(fields=['create_stamp'])
        ]
        unique_together = [['respondent', 'poll']]

    respondent      = models.ForeignKey(Account, on_delete=models.CASCADE)
    poll            = models.ForeignKey(Poll, on_delete=models.CASCADE) #deletes PollResult if Poll is deleted
    choice          = models.BooleanField(null=True)
    create_stamp    = models.DateField(auto_now_add=True)