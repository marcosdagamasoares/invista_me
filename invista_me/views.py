from django.shortcuts import render, redirect
# TRAZER INFORMA��ES DO BANCO PARA A P�GINA
from .models import Investimento
# PARA UTILIZAR O ( forms.py )
# from .forms import nome_formul�rio
from .forms import InvestimentoForm


def investimentos(request):
    # CRIAR DICION�RIO P/PASSAR AS INFORMA��ES DOS BANCO PARA P�GINA
    # Guardo a informa��o dentro da chave ( dados ) do Dicion�rio ( dados )
    dados = {
        'dados': Investimento.objects.all()  # retorna todos os dados da tabela Investimento
    }
    # dados: � passado como par�metro de context
    return render(request, 'investimentos/investimentos_ant.html', context=dados)


# Poderia usar por exemplo: Investimento.objects.get(valor=100)
def detalhe(request, id_investimento):
    # COMO TEMOS QUE PASSAR UM DICION�RIO, TRANSFORMAR EM UM DICION�RIO
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


def criar(request):
    # receber as informa��es dentro da fun��o criar(request)
    # Primeiro saber se estamos criando algo ou alterando a informa��o
    if request.method == 'POST':
        # N�o ser� criado do zero, Usando as informa��es passadas na tela
        investimento_form = InvestimentoForm(request.POST)

        if investimento_form.is_valid():  # Validar se dados est�o corretamente preenchidos
            investimento_form.save()  # Salvar no banco
            # Ap�s ( Salvar ) redirecionar para a p�gina de listam
            # Importar ( redirect ) -  from django.shortcuts import render,HttpResponse , redirect
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()   # Instanciar
        # Criar dicion�rio para passar os dados para a p�gina
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):  # id_investiemnto � um nome qualquer
    # Editar item existente no banco, econtrar um �tem ou nao com este ( id )
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificar qual requisi��o est� sendo feita
    # novo_investimemnto/1 - GET
    if request.method == 'GET':
        # Popular formul�rio e entrega de volta p/tela com infoma��es preenchidas
        formulario = InvestimentoForm(instance=investimento)

        # Retornar para a mesma p�gina que est� sendo usada para criar novos investimentos
        # Formul�rio ser� criado com as informa��es preenchidas
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})

    # caso requisi��o seja POST
    # Verificar se formul�rio foi preenchido corretamente
    # Atualizar informa��o sem criar uma: instance=
    # Usando ( instance ) estou usando algo j� existente

    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)    # InvestimentoForm sendo criado
        # Ver se o formul�rio est� v�lido
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')  # nome da url

# Por padr�o:
# Quando acessa uma p�gina estamos fazendo requisi��o ( GET )
# Quando envia dados a partir de uma p�gina estamos fazendo requisi��o ( POST )
# Quando confirmo uma ( EXCLUS�O ) estou enviando um ( POST )


def excluir(request, id_investimento):
    # Buscar informa��o no banco
    # Exemplo: Poderia usar Investimento.objects.get(data=)
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        # Redirecionar para p�gina de Investimento
        return redirect('investimentos')  # ( investimentos ) � o nome da url
    # Se n�o for ( POST ) est� tentando carregar a p�g pela 1a vez
    # Pedir que confirme a exclus�o, caso clique em ( Confirmar ) estar� fazendo
    # uma postagem, neste caso ser� exclu�da a postagem
    #                        Passar um dicion�rio que cont�m item que receber� investimento
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})


def investimentos2(request):
    investe = {
        'dados_investimento': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos2.html', context=investe)


def detalhe2(request, id_investimento):
    investe = {
        'dados_investimento': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe2.html', investe)
