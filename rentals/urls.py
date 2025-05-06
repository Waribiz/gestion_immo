from rest_framework.routers import DefaultRouter
from .views import ContratViewSet

router = DefaultRouter()
router.register('contrats', ContratViewSet)

urlpatterns = router.urls
