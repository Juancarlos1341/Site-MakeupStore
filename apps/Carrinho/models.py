from operator import mod
from statistics import quantiles
from django.db import models

class Items(models.Model):
    numero_carrinho = models.IntegerField()
    pertence_pessoa = models.CharField(max_length=100)
    produtos = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    preco_final = models.DecimalField(max_digits=100, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'o Item {self.id} foi criado'
    

class Carrinho(models.Model):
    numero = models.IntegerField()
    valor_total = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.numero)