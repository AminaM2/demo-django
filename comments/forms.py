from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['title', 'content', 'anonymous']
  
        labels = {
            'title': 'Titre',
            'content': 'Commentaire',
            'anonymous': 'Ajouter ce commentaire en tant qu\'utilisateur anonyme?'
        }