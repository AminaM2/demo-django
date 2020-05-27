from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account

class AccountForm(UserCreationForm):
    # pwd_help_text = "Votre mot de passe ne doit pas être trop similaire à vos autres informations personnelles.<br>"
    # + "Votre mot de passe doit contenir au moins 8 caractères.<br>"
    # + "Votre mot de passe ne peut pas être un mot de passe couramment utilisé.<br>"
    # + "Votre mot de passe ne peut pas être entièrement numérique."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label     = 'Mot de passe' #password1 and password2 are fields in the form, but not in the model. Therefore, they are treated differently from the fields below.
        self.fields['password2'].label     = 'Confirmation du mot de passe'
        
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text  = '150 caractères ou moins. Lettres, chiffres et @ /. / + / - / _ uniquement.'

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_author')

        labels = {
            'first_name'    : 'Prénom',
            'last_name'     : 'Nom de famille',
            'email'         : 'Adresse email',
            'username'      : 'Nom d\'utilisateur',
            'is_author'     : 'Êtes-vous un(e) auteur(e)?'
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nom d\'utilisateur'
        self.fields['password'].label = 'Mot de passe'