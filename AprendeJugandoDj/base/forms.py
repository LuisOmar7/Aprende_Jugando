from django import forms
from .models import Comentario
 

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['email','mensaje']