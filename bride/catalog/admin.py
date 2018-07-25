# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product


# admin.site.register([Category, Product])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'collection', 'shape', 'style', 'fabric', 'fastener_type', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
