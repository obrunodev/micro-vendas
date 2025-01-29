from apps.empresas.models import Empresa
from django.db import models
from django.utils.text import slugify
from shared.utils import generate_hash_id
from shared.models import BaseModel


class Produto(BaseModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=255)
    slug = models.SlugField()
    id_unico = models.CharField('Identificador único', max_length=6)
    descricao = models.TextField('Descrição', blank=True, null=True)
    preco_custo = models.DecimalField('Preço de custo', default=0, decimal_places=2, max_digits=10)
    preco_venda = models.DecimalField('Preço de venda', default=0, decimal_places=2, max_digits=10)
    quantidade = models.IntegerField('Quantidade em estoque', default=0)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(self.nome)
        self.id_unico = generate_hash_id(self.id, 6)
        super().save(*args, **kwargs)