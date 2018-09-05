from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from catalog.models import Product
from .like import Like
from .forms import LikeAddProductForm


@require_POST
def like_add(request, product_id):
    like = Like(request)
    product = get_object_or_404(Product, id=product_id)
    form = LikeAddProductForm(request.POST)
    if form.is_valid():
        like.add(product)
    return redirect('like:likes_detail')


def like_remove(request, product_id):
    like = Like(request)
    product = get_object_or_404(Product, id=product_id)
    like.remove(product)
    return redirect('like:likes_detail')


def likes_detail(request):
    like = Like(request)
    return render(request, 'like/liked_products.html', {'like': like})
