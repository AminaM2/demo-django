from django.contrib.auth.forms import UserCreationForm
from .models import Account

class AccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_author')

        labels = {
            'first_name'    : 'Prénom',
            'last_name'     : 'Nom de famille',
            'email'         : 'Adresse email',
            'username'      : 'Nom d\'utilisateur',
            'password1'     : 'Mot de passe',
            'password2'     : 'Confirmation du mot de passe',
            'is_author'     : 'Êtes-vous un(e) auteur(e)?'
        }