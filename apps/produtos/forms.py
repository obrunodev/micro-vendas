from apps.produtos.models import Produto
from shared.forms import BaseModelForm


class ProdutoForm(BaseModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_custo', 'preco_venda', 'quantidade']
