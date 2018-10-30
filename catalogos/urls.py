from django.urls import path
from catalogos.views import CategoriaView,CategoriaNew,CategoriaEdit,CategoriaDel

urlpatterns =[
    path('categorias',CategoriaView.as_view(),name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(),name='categoria_new'),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(),name='categoria_edit'),
    path('categoria/delete<int:pk>', CategoriaDel.as_view(),name='categoria_delete'),

]

