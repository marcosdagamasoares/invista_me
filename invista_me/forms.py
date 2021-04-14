from django.forms import ModelForm
# Importar todas as classes que representam tabelas no banco
from .models import Investimento

# Para criar uma ModelForm � preciso criar uma classe
# criar desta forma: nome_classe + Form:  InvestimentoForm

class InvestimentoForm(ModelForm):  # Herdar de ModelForm
    class Meta:
        # Como queremos que este formul�rio seja criado este formul�rio
        model = Investimento
        # Quais campos para exibir na tela
        # Exemplo
        # fields = ['id', 'investimento', 'valor', 'pago']
        fields = '__all__'  # Para exibir todos os campos