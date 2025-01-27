"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.contrib import admin
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
        title="Villa Arzan API",
        default_version='v1',
        description="This is a REST API for Villa Arzan",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="fshima02@gmail.com"),
        license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin-api/', admin.site.urls),
    #! honeypot admin for attacks on admin panel
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    path('', include('user_area.urls', namespace='user_area')),
    path('', include('post_manager.urls', namespace='post_manager')),
    path('', include('blog.urls', namespace='blog')),
    path('admin/clearcache/', include('clearcache.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #? Swagger root 
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
