from django.contrib.auth.models import User
from account.models import Profile
from novels.models import Genero
from django import forms

# Estamos creando esye modelo separado de user para crear los cmapos del modelo User, y colocarle el { required = False }, si le colocamos este atributo al otro modelo de signup esto provocaria que los ususarios tambien se pudieran registrar a la pagina sin un nombre de usuario


class FormUserEdit(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'nickname'
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'xxx@gmail.com'
    }))

    class Meta:
        model = User
        fields = ('username', 'email',)


class Form_edit_profile(forms.ModelForm):
    favorite_genes = forms.ModelMultipleChoiceField(queryset=Genero.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'favorite_genes_input'
    }))

    class Meta:
        model = Profile
        fields = ['social_network', 'about_me',
                  'image_profile', 'favorite_genes']
        widgets = {
            'social_network': forms.TextInput(attrs={
                'class': 'social_network_input',
                'placeholder': '@example'
            }),
            # espacio para diferenciacion de los campos
            'about_me': forms.Textarea(attrs={
                'class': 'about_me_input',
                'placeholder': 'maximo 200 caracteres'
            }),
            'image_profile': forms.ClearableFileInput(attrs={
                'class': 'image_profile_input'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
# Nota no se estan editandolos campos del ususario
