from apps.produtos.models import Produto
from apps.vendas.services.vendas import VendasService
from apps.vendas.models import Carrinho
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView


class PedidosView(LoginRequiredMixin, ListView):
    context_object_name = 'vendas'
    paginate_by = 10

    def get_queryset(self):
        empresa = self.request.empresa_set.first()
        vendas_service = VendasService(empresa=empresa)
        return vendas_service.get_vendas_empresa()


class NovoPedidoView(LoginRequiredMixin, View):
    
    def get(self, request):
        vendas_service = VendasService(empresa=request.user.empresa_set.first())
        context = vendas_service.context_novo_pedido(request)
        return render(request, 'vendas/novo_pedido.html', context)


class CarrinhoView(LoginRequiredMixin, View):
    
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
            resposta = c.adiciona_produto(produto)
            if 'erro' in resposta: messages.error(request, resposta['erro'])
            else: messages.success(request, resposta['message'])
        
        return redirect('vendas:novo_pedido')
