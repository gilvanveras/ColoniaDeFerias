from django import forms
from .models import Associado


class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = '__all__'