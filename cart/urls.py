from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart_home'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('edit/<item_id>/', views.edit_cart, name='edit_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
