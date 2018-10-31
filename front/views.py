from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class SinPrivilegios(PermissionRequiredMixin):
    login_url = 'front:sin_privilegios'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class HomePage(generic.View):
    def get(self,request,*args, **kwargs):
        return HttpResponse('Home page')


#Validacion si el usuario esta autenticado con mixin de  left to the right
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'front/home.html'

    #Si el usuario no esta autenticado se redirija al login
    login_url = 'front:login'

class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'front/sin_privilegios.html'


