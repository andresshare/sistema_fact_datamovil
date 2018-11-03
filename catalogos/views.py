from django.http import HttpResponse
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
    login_url = 'generales:login'


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

def categoria_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    categorias = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Categorías", styles['Heading1'])
    categorias.append(header)
    headings = ('Id', 'Descrición', 'Activo', 'Creación')
    if not pk:
        todascategorias = [(p.id, p.descripcion, p.activo, p.creado)
                           for p in Categoria.objects.all().order_by('pk')]
    else:
        todascategorias = [(p.id, p.descripcion, p.activo, p.creado)
                           for p in Categoria.objects.filter(id=pk)]
    
    t = Table([headings] + todascategorias)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    categorias.append(t)
    doc.build(categorias)
    response.write(buff.getvalue())
    buff.close()
    return response
