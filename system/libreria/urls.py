from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('caballos', views.caballos, name='caballos'),
    path('caballos/crear', views.crear, name='crear')
    ]