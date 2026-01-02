from django import forms
from novels.models import Description


class Makenovel(forms.ModelForm):

    class Meta:
        model = Description
        fields = ('title', 'genero', 'text_description',
                  'prologo', 'author', 'imagen_portada')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'titulo-novel'
            }),
            'genero': forms.CheckboxSelectMultiple(attrs={
                'class': 'genero-inside'
            }),
            'author': forms.CheckboxSelectMultiple(attrs={
                'class': 'titulo-novel'
            }),
            'text_description': forms.Textarea(attrs={
                'class': 'text-description'
            })
        }
