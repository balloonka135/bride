from django.urls import path, re_path
from . import views

app_name = 'like'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.like_remove, name='like_remove'),
    re_path(r'^add/(?P<product_id>\d+)$', views.like_add, name='like_add'),
    re_path(r'^$', views.likes_detail, name='likes_detail')
]
