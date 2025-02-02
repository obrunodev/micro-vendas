from apps.vendas.models import Carrinho, ProdutoCarrinho
from django.contrib import admin


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    ...


@admin.register(ProdutoCarrinho)
class ProdutoCarrinhoAdmin(admin.ModelAdmin):
    ...
