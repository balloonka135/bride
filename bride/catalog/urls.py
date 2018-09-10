from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'catalog'

urlpatterns = [
    re_path(r'^browse/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productDetail, name='ProductDetail'),
    re_path(r'^browse/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_cat'),
    re_path(r'^browse/(?P<category_slug>[-\w]+)/(?P<collection_slug>[\w\-]+)/$', views.product_list, name='product_list_coll'),
    re_path(r'^browse/accessories/$', views.accessList, name='accessList'),
    re_path(r'^browse/$', views.product_list, name='product_list'),
    re_path(r'^about/$', views.about_us, name='about_us'),
    re_path(r'^designers/$', views.designers, name='designers'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
    re_path(r'^contacts/contact_us/$', views.contact_us, name='contact_us'),
    re_path(r'^booking/$', views.booking, name='booking'),
    re_path(r'^booking/book/$', views.book_appoint, name='book_appoint'),
    re_path(r'^search/$', views.ProductSearchListView.as_view(), name='search_plist'),
    re_path(r'^$', views.index, name='index'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
