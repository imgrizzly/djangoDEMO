# _*_ encoding:utf-8 _*_

from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # path(r'^login/', views.login),
]