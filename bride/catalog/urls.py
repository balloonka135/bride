from django.conf.urls import url

from . import views

app_name = 'catalog'
# urlpatterns = [
#     url('', views.index, name='index'),
#     url('publishers/', PublisherList.as_view()),
# ]

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.productList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productDetail, name='ProductDetail'),
    url(r'^$', views.productList, name='ProductList'),
]
