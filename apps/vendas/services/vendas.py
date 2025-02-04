from apps.vendas.models import Venda, ProdutoVendido
from apps.produtos.models import Produto


class VendasService:

    def __init__(self, empresa):
        self.empresa = empresa

    def busca_produtos(self, filtro_nome):
        produtos = []
        if filtro_nome: produtos = Produto.objects.filter(
            empresa=self.empresa,
            nome__icontains=filtro_nome
        )
        return produtos

    def finaliza_venda(self, carrinho):
        ...
