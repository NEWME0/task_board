from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from drf_yasg.openapi import Info
    from drf_yasg.views import get_schema_view
    from rest_framework.permissions import AllowAny

    schema_info = Info(title='Task board', default_version='0.0.0', description='...')
    schema_view = get_schema_view(info=schema_info, public=True, permission_classes=(AllowAny,))

    swagger_view = schema_view.with_ui('swagger')

    urlpatterns += [
        path('', swagger_view)
    ]
