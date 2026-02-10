from account.models import Profile
from novels.models import Genero
from django import forms


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
                'class': 'social_network_input'
            }),
            # espacio para diferenciacion de los campos
            'about_me': forms.Textarea(attrs={
                'class': 'about_me_input'
            }),
            'image_profile': forms.ClearableFileInput(attrs={
                'class': 'genres-grid'
            }),


        }
