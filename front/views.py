from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render


class HomePage(generic.View):
    def get(self,request,*args, **kwargs):
        return HttpResponse('Home page')


class Home(generic.TemplateView):
    template_name = 'base/base.html'
