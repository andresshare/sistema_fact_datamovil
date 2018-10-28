from django.shortcuts import render
from django.views import generic
from catalogos.models import Categoria

class CategoriaView(generic.ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'obj'


