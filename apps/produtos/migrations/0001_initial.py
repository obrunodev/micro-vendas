# Generated by Django 4.2.18 on 2025-01-29 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField()),
                ('id_unico', models.CharField(max_length=6, verbose_name='Identificador único')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('preco_custo', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço de custo')),
                ('preco_venda', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço de venda')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade em estoque')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
