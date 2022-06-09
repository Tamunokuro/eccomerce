import re
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from .models import Category, Product, Book

# Create your views here.


def book_detail(request, slug):
    # category = get_object_or_404(Category, slug=category_slug)
    # singleBook = Book.objects.filter(category=category)
    # mybooks = Book.objects.all()
    singleBook = get_object_or_404(Book, slug=slug, in_stock=True)

    return render(request, 'store/bookDetail.html', {'singleBook': singleBook})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def book_category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    book = Book.objects.filter(category=category)
    return render(request, 'store/book_category.html', {'category': category, 'book': book})


def categories(request):
    return{
        'categories': Category.objects.all()
    }


def books(request):
    # mybooks = Book.books.all()
    return render(request, 'store/books.html')


def allproducts(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, in_stock=True)
    return render(request, 'store/productDetail.html', {'product': product})
