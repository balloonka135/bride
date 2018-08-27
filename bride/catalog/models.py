# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# from djongo import models


# Product category (wedding dresses, prom)
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # objects = models.DjongoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_cat', args=[self.slug])


class Shape(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Dress shape') # силует
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # objects = models.DjongoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_cat', args=[self.slug])  # CREATE ANOTHER URL FOR THIS MODEL!!!!!!


class Style(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Dress style')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # objects = models.DjongoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):  
        return reverse('catalog:product_list_cat', args=[self.slug])


class Collection(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Collection')
    # category = models.EmbeddedModelField(model_container=Category)
    category = models.ForeignKey('Category', related_name='collections', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # objects = models.DjongoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('catalog:product_list_coll', args=[self.category.slug, self.slug])


class Fabric(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Dress fabric') # ткань
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # objects = models.DjongoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('catalog:product_list_cat', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    collection = models.ForeignKey('Collection', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    shape =  models.ForeignKey('Shape', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    style = models.ForeignKey('Style', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    fabric = models.ForeignKey('Fabric', related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    fastener_type = models.CharField(max_length=100, db_index=True, verbose_name='Dress fastener type') # тип застежки
    description = models.TextField(blank=True, verbose_name='Product description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='In stock')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # objects = models.DjongoManager()

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:ProductDetail', args=[self.id, self.slug])


class ProductImage(models.Model):
    image = models.ImageField(upload_to='img/albums/', blank=True, verbose_name='Product image')
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE, null=True)


class MailBox(models.Model):
    username = models.CharField(max_length=200, db_index=True, verbose_name='Client Name')
    phone = models.IntegerField()
    message = models.TextField()
    sender = models.EmailField()
    # objects = models.DjongoManager()

    def __str__(self):
        return self.username


class Appointment(models.Model):
    username = models.CharField(max_length=200, db_index=True, verbose_name='Client Name')
    phone = models.IntegerField()
    message = models.TextField()
    sender = models.EmailField()
    date_of_appoint = models.DateField(null=True, blank=True)
    date_of_wedding = models.DateField(null=True, blank=True)
    # objects = models.DjongoManager()

    def __str__(self):
        return self.username





# to start mongo
# brew services start mongodb