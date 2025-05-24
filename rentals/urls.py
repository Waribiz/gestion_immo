from rest_framework.routers import DefaultRouter
from .views import ContratViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'contrats', ContratViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
