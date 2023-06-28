from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control mt-1',
                'id': 'username',
                'name': 'username',
                'placeholder': 'Логин'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control mt-1',
                'id': 'first_name',
                'name': 'first_name',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control mt-1',
                'id': 'last_name',
                'name': 'last_name',
                'placeholder': 'Фамилия'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control mt-1',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Почта'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control mt-1',
                'id': 'password',
                'name': 'password',
                'placeholder': 'Пароль',
            }),
        }