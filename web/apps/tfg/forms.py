from django import forms
from .models import  News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'url': forms.TextInput(
                    attrs={"class": "form-control",
                            "placeholder": "Introduzca la URL de una noticia"}
        ),
            'esFi': forms.HiddenInput(),
            'alg': forms.RadioSelect(),
            'vector': forms.HiddenInput(),
        }
        fields = ( 'url', 'esFi','algoritmo','vector')
