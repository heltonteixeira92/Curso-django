from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from pypro.base.views import home # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('pypro.base.urls')),
    path('aperitivos/', include('pypro.aperitivos.urls')),
    path('modulos/', include('pypro.modulos.urls')),
    path('turmas/', include('pypro.turmas.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
