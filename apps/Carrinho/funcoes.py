from ast import Try
from math import prod
import re
from .models import *
from django.shortcuts import get_object_or_404
from decimal import Decimal
from Produtos.models import Produtos

def salvar_pedido(quantidade, produto, id):
    '''Salva um Pedido no banco de dados'''
    lista_compra = Items.objects.create(
        numero_carrinho = id,
        pertence_pessoa='Juan',
        produtos= produto.nome_produto,
        preco= produto.preco,
        quantidade= quantidade,
        preco_final= str(int(quantidade) * float(produto.preco))
    )
    lista_compra.save()
    try:
        carrinho = Carrinho.objects.get(numero=id)
    except:
        criar_carrinho(id)
    carrinho.valor_total += Decimal(lista_compra.preco_final)
    carrinho.save()


def criar_carrinho(id):
    '''Cria um novo carrinho caso precise'''
    nova_id = int(id) + 1
    carrinho = Carrinho.objects.create(
        numero = nova_id,
        valor_total = 0.00
    )
    carrinho.save()


def revomer(id, request):
    '''Remove o item do banco de dados e na lista'''
    item = get_object_or_404(Items, pk=id)
    quantidade = item.quantidade
    nome = item.produtos
    valor = item.preco_final
    item.delete()
    lista = request.session['lista_de_compras']
    lista.remove(id)
    request.session['lista_de_compras'] = lista
    return quantidade, nome, valor


def preco_total():
    item = Items.objects.get()
    valor_anterior = 0
    for novo_valor in item:
        valor_total = valor_anterior + float(novo_valor)
        valor_anterior = float(novo_valor)
    
    return valor_total


def verifica_item(produto, id):
    try:
        items = Items.objects.get(produtos=produto, numero_carrinho=id)
        if items.produtos != produto :
            return True
        else :
            return False
    except :
        return False

def alterar_produto_no_carrinho(nome, id, id_carrinho, nova_quantidade, request):
    produto = get_object_or_404(Produtos, nome_produto=nome)
    quantidade, nome, valor = revomer(id, request)
    produto = Produtos.objects.get(nome_produto=nome)
    aumentar_estoque(quantidade, produto.id)
    carrinho = Carrinho.objects.get(numero=id_carrinho)
    carrinho.valor_total -= valor
    carrinho.save()
    salvar_pedido(nova_quantidade, produto, id_carrinho)
    diminuir_estoque(nova_quantidade, produto.id)
    listar_item(request, id_carrinho, nome)

def diminuir_estoque(quantidade, id):
    produto = Produtos.objects.get(pk=id)
    produto.estoque -= int(quantidade)
    produto.save()

def aumentar_estoque(quantidade, id):
    produto = Produtos.objects.get(pk=id)
    produto.estoque += int(quantidade)
    produto.save()


def deletar_todos_os_itens(request, id_carrinho):
    lista = request.session['lista_de_compras']
    lista_2 = lista
    for id_item in lista_2:
        print(id_item)
        quantidade, nome, valor = remover_item(id_item)
        produto = Produtos.objects.get(nome_produto=nome)
        aumentar_estoque(quantidade, produto.id)
        carrinho = Carrinho.objects.get(numero=id_carrinho)
        carrinho.valor_total -= valor
        carrinho.save()
    request.session['lista_de_compras'] = None
    carrinho = get_object_or_404(Carrinho, numero=request.session.get('id_carrinho'))
    carrinho.delete()
    request.session['id_carrinho'] = None
    request.session.modified = True


def listar_item(request, id_carrinho, produto):
    '''Adciona id do item na sessao de lista'''
    item = Items.objects.get(numero_carrinho=id_carrinho, produtos=produto)
    lista = request.session['lista_de_compras']
    lista.append(item.id)
    request.session['lista_de_compras'] = lista

def remover_item(id):
    item = get_object_or_404(Items, pk=id)
    quantidade = item.quantidade
    nome = item.produtos
    valor = item.preco_final
    item.delete()
    return quantidade, nome, valor