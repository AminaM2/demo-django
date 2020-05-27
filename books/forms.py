from django import forms
from .models import Book

class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ['author', 'nb_likes']

		labels = {
			'title'				: 'Titre de l\'oeuvre',
			'summary'			: 'Résumé',
			'category'			: 'Catégorie(s)',
			'price'				: 'Prix',
			'publication_date'	: 'Date de publication'
		}

		widgets = {
            'publication_date': DateInput(),
        }