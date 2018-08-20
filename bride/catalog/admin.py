# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product, Shape, Style, Collection, MailBox, Appointment, Fabric


# admin.site.register([Category, Product])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'collection', 'shape', 'style', 'fabric', 'fastener_type', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}


class ShapeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class StyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
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
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(MailBox, MailBoxAdmin)
admin.site.register(Appointment, AppointmentAdmin)

