from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Book, Product
from account.models import UserBase
from .basket import Basket

# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    user = UserBase(request)
    return render(request, 'store/basket/basketSummary.html', {'basket': basket, 'user': user})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        singleBook_id = int(request.POST.get('singleBookid'))
        singleBook_qty = int(request.POST.get('singleBookqty'))
        book = get_object_or_404(Book, id=singleBook_id)

        basket.add(singleBook=book, bookqty=singleBook_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'bookqty': basketqty})

        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        singleBook_id = int(request.POST.get('singleBookid'))
        basket.delete(singleBook=singleBook_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        singleBook_id = int(request.POST.get('singleBookid'))
        singleBook_qty = int(request.POST.get('singleBookqty'))
        basket.update(singleBook=singleBook_id, bookqty=singleBook_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        print(basketqty)
        print(baskettotal)
        response = JsonResponse({'qty': basketqty, 'total': baskettotal})
        return response
