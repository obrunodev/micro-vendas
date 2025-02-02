from apps.vendas import views
from django.urls import path

app_name = 'vendas'
urlpatterns = [
    path('pedido/', views.pedido, name='pedido'),
]
