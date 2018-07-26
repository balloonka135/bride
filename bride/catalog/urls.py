from django.conf.urls import url

from . import views

app_name = 'catalog'
# urlpatterns = [
#     url('', views.index, name='index'),
#     url('publishers/', PublisherList.as_view()),
# ]

urlpatterns = [
    url(r'^browse/(?P<category_slug>[-\w]+)/$', views.productList, name='ProductListByCategory'),
    url(r'^browse/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productDetail, name='ProductDetail'),
    url(r'^browse/$', views.productList, name='ProductList'),
    # url(r'^browse/wedding-dresses/$', views.index, name='wed-dresses'),
    # url(r'^browse/prom-dresses/$', views.index, name='prom-dresses'),
    # url(r'^browse/accessories/$', views.index, name='accessories'),
    # url(r'^browse/wedding-dresses/(?P<collection_slug>[-\w]+)/$', views.index, name='wed-by-collection'),
    # url(r'^browse/prom-dresses/(?P<collection_slug>[-\w]+)/$', views.index, name='prom-by-collection'),
    # url(r'^about-us/$', views.index, name='about-us'),
    url(r'^$', views.index, name='index'),
]
