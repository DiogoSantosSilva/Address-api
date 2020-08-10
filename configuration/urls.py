from django.contrib import admin
from django.urls import path, reverse, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api/', include('address.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    path('', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]