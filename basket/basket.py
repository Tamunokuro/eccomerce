from store.models import Book
from decimal import Decimal


class Basket():
    """
    A base Basket class, providing some default behaviours that can
    be inherited or overided, as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, singleBook, bookqty):
        """
        Adding and updating the user basket data
        """
        singleBook_id = str(singleBook.id)
        print(singleBook_id)
        if singleBook_id in self.basket:
            self.basket[singleBook_id]['qty'] = bookqty
        else:
            self.basket[singleBook_id] = {
                'price': str(singleBook.price), 'qty': bookqty}

        self.save()

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        """
        Collect the singleBook_id in the session data to query the database
        and return products
        """
        singleBook_ids = self.basket.keys()
        singleBooks = Book.books.filter(id__in=singleBook_ids)
        basket = self.basket.copy()

        for singleBook in singleBooks:
            basket[str(singleBook.id)]['singleBook'] = singleBook

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, singleBook):
        """
        Delete item from session data
        """

        singleBook_id = str(singleBook)
        if singleBook_id in self.basket:
            del self.basket[singleBook_id]
            print(singleBook_id)
            self.save()

    def update(self, singleBook, bookqty):
        singleBook_id = str(singleBook)

        if singleBook_id in self.basket:
            self.basket[singleBook_id]['qty'] = bookqty
        self.save()


    def save(self):
        self.session.modified = True
