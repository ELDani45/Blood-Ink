from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from account.models import Profile


class SignIn(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Nickname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))


class SingUp (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'nickname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'xxx@gmail.com'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya esstá registrado.")
        return email

    class Meta:
        model = User
        # Definimos los campos que se mostrarán
        fields = ("username", "email",)
