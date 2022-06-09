from django.urls import path, include
from . import views

app_name = "store"

urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:category_slug>/',
         views.category_list, name='category_list'),
    path('book_search/<slug:category_slug>/',
         views.book_category_list, name='book_category_list'),
    path('books/', views.books, name='books'),
    path('post/<slug:product_slug>/', views.product_detail, name='product_detail'),


]
