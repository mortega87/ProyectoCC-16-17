from django import forms
from .models import *
class formulario_disco(forms.ModelForm):
    class Meta:
		model=DiscoGenerator
		widgets={
			'artista':forms.TextInput(attrs={'placeholder':'Artista','class' : 'form-field'}),
			'titulo':forms.TextInput(attrs={'placeholder':'Titulo','class' : 'form-field'}),
			'estilo':forms.TextInput(attrs={'placeholder':'Estilo','class' : 'form-field'}),
			}
		fields = ('artista','titulo','estilo','portada')
