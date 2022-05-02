from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import *

def index(request):
    produtos = Produtos.objects.order_by().filter(ativo=True)
    #request.session['id_carrinho'] = None
    print(request.session.get('id_carrinho'))
    
    verifica_estoque()
    dicas_produtos = Dicas_produtos.objects.order_by().filter(publicar_dica=True)
    carrosel = Carrossel.objects.order_by()
    dados = {
        'produtos': produtos,
        'dicas': dicas_produtos,
        'carrossel': carrosel
    }
    return render(request, 'produtos/index.html', dados)

def lista_produtos_categoria(request, id):
    
    categoria = get_object_or_404(Categoria, pk=id)
    produtos = Produtos.objects.order_by().filter(categoria=id).filter(ativo=True)

    if 'busca' in request.GET:
        nome_a_buscar = request.GET['busca']
        lista_produtos = produtos.filter(nome_produto__icontains=nome_a_buscar)

        dados = {
            'produtos' : lista_produtos,
            'categoria': categoria,
        }

        return render(request, 'produtos/lista-produtos.html', dados)
    else:
        dados = {
            'produtos' : produtos,
            'categoria': categoria,
        }

        return render(request, 'produtos/lista-produtos.html', dados)

def listagem(request):
    categorias = Categoria.objects.order_by().filter(publicada=True)
    dados = {
        'categorias': categorias
    }
    return render(request, 'produtos/lista-categoria.html', dados)



def produtos(request, id):
    produto_espfico = get_object_or_404(Produtos, pk=id)

    dados = {
        'produto': produto_espfico,
    }

    return render(request, 'produtos/produto.html', dados)


def verifica_estoque():
    for i in range(1, len(Produtos.objects.order_by())):
        produto = Produtos.objects.get(pk=i)
        if produto.estoque == 0:
            produto.ativo = False
            produto.save()