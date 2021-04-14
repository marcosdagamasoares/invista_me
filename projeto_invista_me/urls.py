"""projeto_invista_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me import views


# name='contato' <-- IDENTIFICAR ESSA PÁGINA NA APLICAÇÃO

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', views.investimentos2, name='investimentos2'),
    path('', views.investimentos, name='investimentos'),  #  será Página Inicial por causa 2 aspas
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', views.excluir, name='excluir'),

    # O CAMINHO INICIAL É A PÁGINA INICIAL, IREMOS PARTIR DO ZERO PORQUE A PÁGINA DE
    # LISTAGEM JÁ ESTÁ DENTRO DA PÁGINA INICIAL, COLOCAR APENAS path('/<int:id_investimento>
    # ( id_investimento ) FOI DEFINIDO EM def detalhe(request, id_investimento):
    # PORQUE ESTAMOS RECEBENDO O ( Id ) COMO PARÂMETRO
    # O NOME ( detalhe ) É USAOD DENTRO DE ( investimentos_ant.html )
    # ==================================================================
    # o path abaixo dará aviso
    # ?: (urls.W002) Your URL pattern '/<int:id_investimento>' [name='detalhe'] has a
    #  route beginning with a '/'. Remove this slash as it is unnecessary.
    #  If this pattern is targeted in an include(), ensure the include()
    #  pattern has a trailing '/'.
    # path('/<int:id_investimento>', views.detalhe, name='detalhe'),

    # path('<int:id_investimento>', views.detalhe2, name='detalhe2'),
    path('<int:id_investimento>', views.detalhe, name='detalhe'),

]
