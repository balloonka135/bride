# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
from djongo import models


# Product category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    objects = models.DjongoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Wedding dress
class Product(models.Model):
    category = models.EmbeddedModelField(model_container=Category)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Name')
    slug = models.CharField(max_length=200, db_index=True)
    collection = models.CharField(max_length=200, db_index=True, verbose_name='Collection')
    shape = models.CharField(max_length=100, db_index=True, verbose_name='Dress shape') # силует 
    style = models.CharField(max_length=100, db_index=True, verbose_name='Dress style')
    fabric = models.CharField(max_length=100, db_index=True, verbose_name='Dress fabric') # ткань
    fastener_type = models.CharField(max_length=100, db_index=True, verbose_name='Dress fastener type') # тип застежки
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Product image')
    description = models.TextField(blank=True, verbose_name='Product description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='In stock')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    objects = models.DjongoManager()

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


# to start mongo
# brew services start mongodb