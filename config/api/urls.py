from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = 'api'

urlpatterns = []

if settings.DEBUG:
    from django.conf.urls import url

    schema_view = get_schema_view(
        openapi.Info(
            title="EMAILVERIFIER API",
            default_version='v1',
            description="API for GLADE",
            terms_of_service="about:blank",
            contact=openapi.Contact(email="mail@mail.com"),
            license=openapi.License(name="My  License"),
        ),
        urlconf='config.api.swagger_urls',
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
