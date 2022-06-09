from django import views
from django.urls import path
from . import views


app_name = "basket"

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),
    path('delete-item/', views.basket_delete, name='basket_delete'),
    path('update/', views.basket_update, name='basket_update')
]
