from apps.vendas.models import Carrinho, Venda, ProdutoVendido
from apps.produtos.models import Produto


class VendasService:

    def __init__(self, empresa):
        self.empresa = empresa
    
    def get_vendas_empresa(self):
        return Venda.objects.filter(empresa=self.empresa)

    def carrega_carrinho(self, request):
        return Carrinho.objects.filter(
            usuario=request.user,
            empresa=request.user.empresa_set.first()
        ).first()

    def busca_produtos(self, filtro_nome):
        produtos = []
        if filtro_nome: produtos = Produto.objects.filter(
            empresa=self.empresa,
            nome__icontains=filtro_nome
        )
        return produtos
    
    def context_novo_pedido(self, request):
        return {
            'produtos': self.busca_produtos(
                filtro_nome=request.GET.get('q')
            ),
            'carrinho': self.carrega_carrinho(request),
        }

    def finaliza_venda(self, carrinho):
        ...
