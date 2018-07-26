# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product, Shape, Style, Fabric, Collection


def index(request):
    return render(request, 'catalog/index.html', {})


def productList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    collections = Collection.objects.all()
    products = Product.objects.all()
    shapes = Shape.objects.all()
    styles = Style.objects.all()
    fabrics = Fabric.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/product_list.html', {
        'category': category,
        'categories': categories,
        'collections': collections,
        'products': products,
        'shapes': shapes, 
        'styles': styles, 
        'fabrics': fabrics
    })


def productDetail(request, id, slug):
    product = get_object_or_404(Product, pk=id, slug=slug)
    return render(request, 'catalog/product_detail.html', {
        'product': product
    })


# class ProductList(ListView):
#     template_name = 'catalog/product_list.html'
#     paginate_by = 10

#     def get_queryset(self):
#         self.category = None
#         if self.kwargs['category_slug']:
#             self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
#         return Product.objects.filter(category=self.category)


# class ProductDetail(DetailView):

#     model = Product
#     template_name = 'catalog/product_detail.html'
#     pk_url_kwarg = "p_key"
#     slug_url_kwarg = 'slug'
#     query_pk_and_slug = True