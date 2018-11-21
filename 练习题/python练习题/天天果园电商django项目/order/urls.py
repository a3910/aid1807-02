"""FruitDay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from order import views

urlpatterns = [
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^add/(\d+)/(\d+)/$',views.add,name='add'),
    url(r'^list/(\d+)/(\d+)$',views.list),
    url(r'^mycart_count/$',views.mycart_count),
    url(r'^cart_delete_(\d+)/$',views.cart_delete),
    url(r'^edit_(\d+)_(\d+)/$',views.edit),
    url(r'^place_order/$',views.place_order),
    url(r'^order_handle/$',views.order_handle),
]
