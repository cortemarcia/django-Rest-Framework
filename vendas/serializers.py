from rest_framework import serializers
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from vendas.models import Venda


class VendaSerializer(serializers.Serializer):
    produto=ProdutoSerializer()
    deconto= serializers.IntegerField()
    forma= serializers.ChoiceField(choices=Venda.formas)
    valor_total= serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        produto_data= validated_data.pop('produto')
        produto =Produto.objects.get(id=produto_data['id'])
        desconto = validated_data.get('desconto')
        valor_total= produto.valor*(1-desconto/100)
        venda= Venda.objects.create(produto=produto, valor_total=valor_total,**validated_data)
        return venda

