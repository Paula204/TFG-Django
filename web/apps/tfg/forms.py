from django import forms
from .models import  News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ( 'url',)
        widgets = {
            'url': forms.TextInput(
                    attrs= {"class" : "form-control",
                            "placeholder" : "Introduzca la URL de una noticia"}
        ),
        }