from django.db import models
from produtos.models import Produto
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    desconto = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    formas = (('BOLETO', 'Boleto'),('CARTAO','Cartao'))
    forma= models.CharField(max_length=50, choices= formas)



