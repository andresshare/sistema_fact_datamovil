from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalogos.models import Categoria
from catalogos.forms import CategoriaForm


class CategoriaView(generic.ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'obj'


class CategoriaNew(generic.CreateView):
    model=Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")


class CategoriaEdit(generic.UpdateView):
    model=Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")

class CategoriaDel(generic.DeleteView):
    model = Categoria
    template_name = "catalogos/catalogos_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalogos:categoria_list")






