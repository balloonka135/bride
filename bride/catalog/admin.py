# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product, Shape, Style, Collection, MailBox, Appointment, Fabric, ProductImage


# admin.site.register([Category, Product])

class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [CollectionInline, ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'shape', 'style', 'fabric', 'collection', 'thumbnail', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'thumbnail']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ProductImageInline, ]


class ShapeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class StyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class FabricAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class MailBoxAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'message', 'sender']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'message', 'sender', 'date_of_appoint', 'date_of_wedding']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(MailBox, MailBoxAdmin)
admin.site.register(Appointment, AppointmentAdmin)
