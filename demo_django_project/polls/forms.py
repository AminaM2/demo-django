from django import forms
from .models import Poll, PollResult

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

        exclude = ['poller']
  
        labels = {
            'book': 'Livre',
            'is_active': 'Le sondage est-il actif?'
        }

class PollResultForm(forms.ModelForm):
    class Meta:
        model = PollResult

        fields = ['choice']

        labels = {
            'choice': 'Choix'
        }