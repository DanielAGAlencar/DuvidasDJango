from django import forms
from duvidas.models import Duvida


class DuvidaForm(forms.ModelForm):
    class Meta:
        model = Duvida
        fields = ['descricao', 'nivel', 'data',
                  'nome_aluno', 'nome_professor', 'tipo']
