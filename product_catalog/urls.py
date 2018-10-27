from django.urls import path

from product_catalog.views import CategoriaView

urlpatterns = [
    path('categorias', CategoriaView.as_view(),name='categoria_list')
]
