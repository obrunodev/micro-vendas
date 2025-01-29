from apps.empresas.models import Empresa
from django.contrib import admin


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    ...
