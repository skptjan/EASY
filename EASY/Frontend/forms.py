from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from django import forms
from .models import PLANS, Lamp


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=254,
                             widget=TextInput(attrs={'placeholder': 'Email', 'autocomplete': 'off'}))
    username = forms.CharField(label='',
                               widget=TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}))
    # first_name = forms.CharField(label='',
    #                              widget=TextInput(attrs={'placeholder': 'Voornaam', 'autocomplete': 'off'}))
    # last_name = forms.CharField(label='',
    #                             widget=TextInput(attrs={'placeholder': 'Achternaam', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='',
                                widget=PasswordInput(attrs={'placeholder': 'Wachtwoord', 'autocomplete': 'off'}))
    password2 = forms.CharField(label='', widget=PasswordInput(
        attrs={'placeholder': 'Herhaal wachtwoord', 'autocomplete': 'off'}))
    plan = forms.CharField(max_length=20, widget=forms.Select(choices=PLANS))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'plan')


class LampForm(forms.ModelForm):
    class Meta:
        model = Lamp
        fields = ['lamp_name', 'time_set_on', 'time_set_off']
