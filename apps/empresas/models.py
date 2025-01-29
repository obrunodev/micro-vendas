from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel


class Empresa(BaseModel):
    nome = models.CharField('Nome da empresa', max_length=255)
    usuarios = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nome
