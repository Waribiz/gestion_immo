from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# This code defines the URL patterns for the Property API using Django REST Framework's router.
# It registers the PropertyViewSet with the router, allowing for standard CRUD operations on the Property model.