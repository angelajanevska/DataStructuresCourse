from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Лозинка', 'class': 'inputs'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Повтори лозинка', 'class': 'inputs'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Корисничко име', 'class': 'inputs'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Име', 'class': 'inputs'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Презиме', 'class': 'inputs'}),
            'email': forms.TextInput(attrs={'placeholder': 'Е-мајл адреса', 'class': 'inputs'}),
        }
