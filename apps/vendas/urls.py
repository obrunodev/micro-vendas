from apps.vendas import views
from django.urls import path

app_name = 'vendas'
urlpatterns = [
    path('pedidos/', views.PedidosView.as_view(), name='pedidos'),
    path('novo-pedido/', views.NovoPedidoView.as_view(), name='novo_pedido'),
    path('carrinho/', views.CarrinhoView.as_view(), name='carrinho'),
]
