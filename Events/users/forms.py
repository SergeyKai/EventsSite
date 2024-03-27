from django import forms
from django.contrib.auth.forms import UsernameField, ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        field_classes = {"username": UsernameField}


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label='Пароль',
        help_text=f"""
        Пароли хранятся в зашифрованном виде, поэтому нет 
        возможности посмотреть пароль этого пользователя, но вы 
        можете изменить его используя
        <a href="/change-password/">эту форму</a>..
        """
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", 'photo')
        field_classes = {"username": UsernameField}
