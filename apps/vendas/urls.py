from apps.vendas import views
from django.urls import path

app_name = 'vendas'
urlpatterns = [
    # path('pedido/', views.pedido, name='pedido'),
    path('pedido/', views.PedidoView.as_view(), name='pedido'),
    path('finaliza-venda/', views.FinalizaVendaView.as_view(), name='finaliza_venda'),
]
