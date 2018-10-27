from django.shortcuts import render
from django.views import generic
from product_catalog.models import Categoria


class CategoriaView(generic.ListView):
    model = Categoria
    template_name = 'product_catalog/categoria_list.html'
    context_object_name = 'obj'

