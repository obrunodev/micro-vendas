from apps.produtos.models import Produto
from apps.empresas.models import Empresa
from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel


class Venda(BaseModel):
    nome_cliente = models.CharField('Nome do cliente', max_length=255, blank=True, null=True)
    valor_total = models.DecimalField('Valor da venda', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
    def __str__(self):
        return f'{ self.nome_cliente } - R$ { self.valor_total } - Data: { self.created_at }'


class ProdutoVendido(BaseModel):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    nome_produto = models.CharField('Nome do produto', max_length=255)
    valor_produto = models.DecimalField('Valor do produto', max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)

    class Meta:
        verbose_name = 'Produto vendido'
        verbose_name_plural = 'Produtos vendidos'
    
    def __str__(self):
        return f'{ self.nome_produto } - R$ { self.valor_produto } - Qtd: { self.quantidade }'


class Carrinho(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valor_total = models.DecimalField('Valor totar', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'
    
    def __str__(self):
        return f'Carrinho: {self.empresa} - {self.usuario}'
    
    def adiciona_produto(self, produto):
        produtos_no_carrinho = self.produtos.all()
        if produto.id_unico in [p.produto.id_unico for p in produtos_no_carrinho]:
            return False
        ProdutoCarrinho.objects.create(
            produto=produto,
            carrinho=self,
        )
        self.valor_total = sum([
            produto.produto.preco_venda
            for produto in self.produtos.all()
        ])
        self.save()
        return True


class ProdutoCarrinho(BaseModel):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='produtos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:
        ordering = ['produto__nome']
        verbose_name = 'Produto do carrinho'
        verbose_name_plural = 'Produtos do carrinho'

    def __str__(self):
        return f'{self.carrinho} - {self.produto}'
