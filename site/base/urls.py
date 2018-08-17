"""site URL Configuration"""

from django.conf.urls import include, url, handler404, \
    handler500, handler403, handler400
from django.urls import path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from apps.pages.views import ErrorPageView


urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^clothes/', include('apps.clothes.urls')),
    path('', include('apps.pages.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# views to display the corresponding error pages
handler404 = ErrorPageView.as_view(error_code='404')
handler403 = ErrorPageView.as_view(error_code='403')
handler400 = ErrorPageView.as_view(error_code='400')
handler500 = ErrorPageView.as_view(error_code='500')
