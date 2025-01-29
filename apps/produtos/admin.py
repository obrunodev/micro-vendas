from apps.produtos.models import Produto
from django.contrib import admin


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'id_unico']
    search_fields = ['nome', 'id_unico']