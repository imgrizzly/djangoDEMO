# _*_ encoding:utf-8 _*_

from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('welcome/', views.welcome, name='welcome'),
    path('orderlist/', views.orderlist, name='orderlist'),
    path('orderadd/', views.orderadd, name='orderadd'),
    path('memberlist/', views.memberlist, name='memberlist'),
    path('memberlistdata/', views.memberlistdata, name='memberlistdata'),
    # path(r'^login/', views.login),
]
