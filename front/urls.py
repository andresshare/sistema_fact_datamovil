from django.urls import path
from front.views import Home

urlpatterns = [
    path('', Home.as_view(),name='home'),

]