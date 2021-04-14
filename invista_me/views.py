from django.shortcuts import render, redirect
# TRAZER INFORMAÇÕES DO BANCO PARA A PÁGINA
from .models import Investimento
# PARA UTILIZAR O ( forms.py )
# from .forms import nome_formulário
from .forms import InvestimentoForm


def investimentos(request):
    # CRIAR DICIONÁRIO P/PASSAR AS INFORMAÇÕES DOS BANCO PARA PÁGINA
    # Guardo a informação dentro da chave ( dados ) do Dicionário ( dados )
    dados = {
        'dados': Investimento.objects.all()  # retorna todos os dados da tabela Investimento
    }
    # dados: é passado como parâmetro de context
    return render(request, 'investimentos/investimentos_ant.html', context=dados)


# Poderia usar por exemplo: Investimento.objects.get(valor=100)
def detalhe(request, id_investimento):
    # COMO TEMOS QUE PASSAR UM DICIONÁRIO, TRANSFORMAR EM UM DICIONÁRIO
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


def criar(request):
    # receber as informações dentro da função criar(request)
    # Primeiro saber se estamos criando algo ou alterando a informação
    if request.method == 'POST':
        # Não será criado do zero, Usando as informações passadas na tela
        investimento_form = InvestimentoForm(request.POST)

        if investimento_form.is_valid():  # Validar se dados estão corretamente preenchidos
            investimento_form.save()  # Salvar no banco
            # Após ( Salvar ) redirecionar para a página de listam
            # Importar ( redirect ) -  from django.shortcuts import render,HttpResponse , redirect
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()   # Instanciar
        # Criar dicionário para passar os dados para a página
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):  # id_investiemnto é um nome qualquer
    # Editar item existente no banco, econtrar um ítem ou nao com este ( id )
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificar qual requisição está sendo feita
    # novo_investimemnto/1 - GET
    if request.method == 'GET':
        # Popular formulário e entrega de volta p/tela com infomações preenchidas
        formulario = InvestimentoForm(instance=investimento)

        # Retornar para a mesma página que está sendo usada para criar novos investimentos
        # Formulário será criado com as informações preenchidas
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})

    # caso requisição seja POST
    # Verificar se formulário foi preenchido corretamente
    # Atualizar informação sem criar uma: instance=
    # Usando ( instance ) estou usando algo já existente

    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)    # InvestimentoForm sendo criado
        # Ver se o formulário está válido
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')  # nome da url

# Por padrão:
# Quando acessa uma página estamos fazendo requisição ( GET )
# Quando envia dados a partir de uma página estamos fazendo requisição ( POST )
# Quando confirmo uma ( EXCLUSÂO ) estou enviando um ( POST )


def excluir(request, id_investimento):
    # Buscar informação no banco
    # Exemplo: Poderia usar Investimento.objects.get(data=)
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        # Redirecionar para página de Investimento
        return redirect('investimentos')  # ( investimentos ) é o nome da url
    # Se não for ( POST ) está tentando carregar a pág pela 1a vez
    # Pedir que confirme a exclusão, caso clique em ( Confirmar ) estará fazendo
    # uma postagem, neste caso será excluída a postagem
    #                        Passar um dicionário que contém item que receberá investimento
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
