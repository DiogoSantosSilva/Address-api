from django.contrib import admin
from django.urls import path, reverse, include, re_path
from django.contrib.auth import views
from rest_framework import routers
from configuration import settings
from address.views import (CountryViewSet, StateViewSet, CityViewSet,
                           NeighbourhoodViewSet, AddressViewSet)

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'state', StateViewSet)
router.register(r'city', CityViewSet)
router.register(r'neighbourhood', NeighbourhoodViewSet)
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
]