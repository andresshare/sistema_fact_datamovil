from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalogos.models import Categoria, SubCategoria, Producto
from catalogos.forms import CategoriaForm, SubCategoriaForm, ProductoForm
from front.views import SinPrivilegios

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj"
    login_url = 'front:login'


class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")
    success_message="Categoría Creada Satisfactoriamente"


class CategoriaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_categoria"
    model=Categoria
    template_name="catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class=CategoriaForm
    success_url= reverse_lazy("catalogos:categoria_list")


class CategoriaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_categoria"
    model=Categoria
    template_name="catalogos/catalogos_del.html"
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:categoria_list")
    

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "catalogos/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'front:login'


class SubCategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_subcategoria"
    model=SubCategoria
    template_name="catalogos/subcategoria_form.html"
    context_object_name = 'obj'
    form_class=SubCategoriaForm
    success_url= reverse_lazy("catalogos:subcategoria_list")
    success_message="Sub Categoría Creada Satisfactoriamente"

 
class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_subcategoria"
    model = SubCategoria
    template_name = "catalogos/subcategoria_form.html"
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("catalogos:subcategoria_list")
    success_message="Sub Categoría Actualizada Satisfactoriamente"

class SubCategoriaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_subcategoria"
    model=SubCategoria
    template_name="catalogos/catalogos_del.html"
    context_object_name = 'obj'
    success_url= reverse_lazy("catalogos:subcategoria_list")


class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"
    login_url = 'front:login'


class ProductoNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_produco"
    model=Producto
    template_name="catalogos/producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("catalogos:producto_list")
    success_message="Producto Creado Satisfactoriamente"


class ProductoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name = "catalogos/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("catalogos:producto_list")
    success_message="Producto Modificado Satisfactoriamente"