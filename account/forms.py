from account.models import Profile
from django import forms


class Form_edit_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['social_network', 'about_me', 'image_profile']
        widgets = {
            'social_network': forms.TextInput(attrs={
                'class': 'social_network_input'
            }),
            # espacio para diferenciacion de los campos
            'about_me': forms.Textarea(attrs={
                'class': 'about_me_input'
            }),
            'image_profile': forms.ClearableFileInput(attrs={
                'class': 'image_profile_input'
            })

        }
