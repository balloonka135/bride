from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^catalog/', include('catalog.urls', namespace='catalog'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url('polls/', include('polls.urls')),
#     url('admin/', admin.site.urls),
# ]
