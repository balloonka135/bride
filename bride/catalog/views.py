# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from .models import Category, Product, Shape, Style, Fabric, Collection, MailBox, Appointment, ProductImage
from .forms import ContactUsForm, BookAppointForm
from .filters import WeddingCollectionFilter, EveningCollectionFilter


def index(request):
    # query embedded fields
    # entries = Entry.objects.filter(blog={'name': 'Beatles Blog'})
    collections = Collection.objects.all()
    return render(request, 'catalog/index.html', {'collections': collections})


def about_us(request):
    return render(request, 'catalog/about_us.html', {})


def designers(request):
    return render(request, 'catalog/designers.html', {})


def contacts(request):
    return render(request, 'catalog/contacts.html', {})


def booking(request):
    return render(request, 'catalog/book_appointment.html', {})


def product_list(request, category_slug=None, collection_slug=None):
    category = None
    collection = None
    categories = Category.objects.all()
    collections = Collection.objects.all()
    products = Product.objects.all()
    shapes = Shape.objects.all()
    styles = Style.objects.all()
    fabrics = Fabric.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collection=collection)

    if category.slug == 'wedding_dress':
        collection_filter = WeddingCollectionFilter(request.GET, queryset=products)
    else:
        collection_filter = EveningCollectionFilter(request.GET, queryset=products)
    return render(request, 'catalog/product_list.html', {
        'category': category,
        'collection': collection,
        'categories': categories,
        'collections': collections,
        'products': products,
        'shapes': shapes,
        'styles': styles,
        'fabrics': fabrics,
        'filter': collection_filter
    })


def productDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    images = product.p_images.all()
    rec_products = Product.objects.filter(collection=product.collection)  # products from same collection
    rec_products = Product.objects.exclude(slug=product.slug)
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'images': images,
        'related_products': rec_products
    })


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():  # All validation rules pass
            contact_form.save(commit=True)

            subject = 'Adelini MailBox'
            sender = contact_form.cleaned_data['sender']
            message = contact_form.cleaned_data['message']
            username = contact_form.cleaned_data['username']
            phone = contact_form.cleaned_data['phone']
            recipients = ['adelini.wedding.dress@gmail.com']

            MailBox.objects.create(username=username, phone=phone, sender=sender, message=message)

            # add extra info to e-mail
            message += '\r\n\r\n\r\nПисьмо было отправлено с сайта wwww.adelini.wedding.com.ua\r\nАдрес для ответа: {} \r\nИмя клиента: {} \r\nТелефон: +380{} \r\n'.format(sender, username, phone)

            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except:
                send_mail(subject, message, sender, recipients, fail_silently=False)

            # return render_to_response('catalog/success.html', context_instance=RequestContext(request))
            return render(request, 'catalog/success.html')
    # print(contact_form.errors)
    return render(request, 'catalog/fail.html')


def book_appoint(request):
    if request.method == 'POST':
        contact_form = BookAppointForm(request.POST)
        if contact_form.is_valid():  # All validation rules pass
            contact_form.save(commit=True)
            subject = 'Adelini Booking'
            sender = contact_form.cleaned_data['sender']
            message = contact_form.cleaned_data['message']
            username = contact_form.cleaned_data['username']
            phone = contact_form.cleaned_data['phone']
            date_of_appoint = contact_form.cleaned_data['date_of_appoint']
            date_of_wedding = contact_form.cleaned_data['date_of_wedding']
            recipients = ['adelini.wedding.dress@gmail.com']

            Appointment.objects.create(username=username, phone=phone, sender=sender,
                message=message, date_of_appoint=date_of_appoint, date_of_wedding=date_of_wedding
            )

            # add extra info to e-mail
            message += '\r\n\r\n\r\nПисьмо было отправлено с сайта wwww.adelini.wedding.com.ua\r\nАдрес для ответа: {} \r\nИмя клиента: {} \r\nТелефон: +380{} \r\nДата примерки: {}\r\nДата свадьбы: {}\r\n'.format(sender, username, phone, date_of_appoint, date_of_wedding)

            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            # return render_to_response('catalog/success.html', context_instance=RequestContext(request))
            return render(request, 'catalog/success.html')
        else:
            print(contact_form.errors)
            return render(request, 'catalog/fail.html')
    else:
        contact_form = BookAppointForm()

    return redirect(reverse('book_appoint'))


def accessList(request):
    pass






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