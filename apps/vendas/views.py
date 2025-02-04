from apps.produtos.models import Produto
from apps.vendas.services.vendas import VendasService
from apps.vendas.models import Carrinho, ProdutoCarrinho
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View


class PedidoView(View):
    
    def get(self, request):
        vendas_service = VendasService(empresa=request.user.empresa_set.first())
        produtos_filtrados = vendas_service.busca_produtos(
            filtro_nome=request.GET.get('q')
        )
        carrinho = Carrinho.objects.filter(
            usuario=request.user,
            empresa=request.user.empresa_set.first()
        ).first()
        context = {
            'produtos': produtos_filtrados,
            'carrinho': carrinho,
        }
        return render(request, 'vendas/pedido.html', context)
    
    def post(self, request):
        c, created = Carrinho.objects.get_or_create(
            usuario=request.user,
            empresa=request.user.empresa_set.first(),
        )
        if 'limpar_carrinho' in request.POST:
            c.delete()
            messages.success(request, 'Carrinho foi limpo!')
        
        if 'add_carrinho' in request.POST:
            produto_id = request.POST.get('add_carrinho')
            produto = Produto.objects.filter(id=produto_id).first()
            if c.adiciona_produto(produto):
                messages.success(request, 'Produto adicionado ao carrinho!')
        
        return redirect('vendas:pedido')


@login_required
def pedido(request):
    """
    Carrega os produtos, monta carrinho e finaliza a venda.
    """
    vendas_service = VendasService(empresa=request.user.empresa_set.first())
    if request.method == 'GET':
        produtos_filtrados = vendas_service.busca_produtos(
            filtro_nome=request.GET.get('q')
        )
        carrinho = Carrinho.objects.filter(
            usuario=request.user,
            empresa=request.user.empresa_set.first()
        ).first()
        context = {
            'produtos': produtos_filtrados,
            'carrinho': carrinho,
        }
        return render(request, 'vendas/pedido.html', context)
    
    if request.method == 'POST':
        c, created = Carrinho.objects.get_or_create(
            usuario=request.user,
            empresa=request.user.empresa_set.first(),
        )
        if 'limpar_carrinho' in request.POST:
            c.delete()
            messages.success(request, 'Carrinho foi limpo!')
        
        if 'add_carrinho' in request.POST:
            produto_id = request.POST.get('add_carrinho')
            produto = Produto.objects.filter(id=produto_id).first()
            ProdutoCarrinho.objects.create(
                carrinho=c,
                produto=produto
            )
            c.valor_total = sum([
                produto.produto.preco_venda for produto in ProdutoCarrinho.objects.filter(
                    carrinho=c
                )
            ])
            c.save()
            messages.success(request, 'Produto adicionado ao carrinho!')
        
        return redirect('vendas:pedido')


class FinalizaVendaView(LoginRequiredMixin, View):

    def get(self, request):
        ...
    
    def post(self, request):
        ...
