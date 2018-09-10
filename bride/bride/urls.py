from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    re_path(r'^catalog/', include('catalog.urls', namespace='catalog')),
    re_path(r'^like/', include('like.urls', namespace='like')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
