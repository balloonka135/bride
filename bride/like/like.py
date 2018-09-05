from decimal import Decimal
from django.conf import settings
from catalog.models import Product


class Like(object):
    def __init__(self, request):
        self.session = request.session
        like = self.session.get(settings.LIKE_SESSION_ID)
        if not like:
            like = self.session[settings.LIKE_SESSION_ID] = {}
        self.like = like

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.like:
            self.like[product_id] = {'name': product.name}
        self.save()

    def save(self):
        self.session[settings.LIKE_SESSION_ID] = self.like
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.like:
            del self.like[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.like.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.like[str(product.id)]['product'] = product
        for item in self.like.values():
            yield item

    def __len__(self):
        return len(self.like.values())

    def clear(self):
        del self.session[settings.LIKE_SESSION_ID]
        self.session.modified = True
