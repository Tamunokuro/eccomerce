from .models import Category, Book


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def books(request):
    return{
        'mybooks': Book.objects.all()
    }
