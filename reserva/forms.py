
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['nome_empresa', 'cnpj', 'categoria_empresa', 'stand', 'quitado']
        widgets = {
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'stand': forms.Select(attrs={'class':'form-control'}),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-checkbox-input'}),
        }