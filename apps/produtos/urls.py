from django.urls import path
from apps.produtos import views


app_name = 'produtos'
urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='list'),
    path('create/', views.ProdutoCreateView.as_view(), name='create'),
    path('<str:id_unico>/<str:slug>/update/', views.ProdutoUpdateView.as_view(), name='update'),
    path('<str:id_unico>/<str:slug>/delete/', views.ProdutoDeleteVIew.as_view(), name='delete'),
]