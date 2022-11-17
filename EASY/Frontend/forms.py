from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=254, help_text='Required. Inform a valid email address.',
                             widget=TextInput(attrs={'placeholder': 'Email', 'autocomplete': 'off'}))
    username = forms.CharField(label='',
                               widget=TextInput(attrs={'placeholder': 'Gebruikersnaam', 'autocomplete': 'off'}))
    first_name = forms.CharField(label='',
                               widget=TextInput(attrs={'placeholder': 'Voornaam', 'autocomplete': 'off'}))
    last_name = forms.CharField(label='',
                               widget=TextInput(attrs={'placeholder': 'Achternaam', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='',
                                widget=PasswordInput(attrs={'placeholder': 'Wachtwoord', 'autocomplete': 'off'}))
    password2 = forms.CharField(label='', widget=PasswordInput(
        attrs={'placeholder': 'Herhaal wachtwoord', 'autocomplete': 'off'}))

    # PlanKeuze = [
    #     ('Starter', 'Starter'),
    #     ('Regular', 'Regular'),
    #     ('Advanced', 'Advanced'),
    # ]
    #
    # Plan = forms.ChoiceField(choices=PlanKeuze, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
