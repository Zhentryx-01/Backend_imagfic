from django.urls import path, re_path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Imagfic API",
        default_version='v1',
        description="API documentation for Imagfic backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@imagfic.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    url="https://backend-imagfic.onrender.com",
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]  # Disable Django session login
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    
    # Swagger documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

