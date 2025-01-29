from apps.produtos.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 10

    def get_queryset(self):
        usuario = self.request.user
        empresa = usuario.empresa_set.first()  # FIXME Isso deverá ser multi empresa
        return Produto.objects.filter(empresa=empresa)


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco_custo', 'preco_venda', 'quantidade']
    success_url = reverse_lazy('produtos:list')

    def form_valid(self, form):
        usuario = self.request.user
        empresa = usuario.empresa_set.first()
        form.instance.empresa = empresa
        return super().form_valid(form)


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco_custo', 'preco_venda', 'quantidade']
    success_url = reverse_lazy('produtos:list')

    def get_object(self, queryset = None):
        id_unico = self.kwargs['id_unico']
        slug = self.kwargs['slug']
        return get_object_or_404(Produto, id_unico=id_unico, slug=slug)


class ProdutoDeleteVIew(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos:list')

    def get_object(self, queryset = None):
        id_unico = self.kwargs['id_unico']
        slug = self.kwargs['slug']
        return get_object_or_404(Produto, id_unico=id_unico, slug=slug)
