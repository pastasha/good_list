from rest_framework.routers import DefaultRouter

from .views import LegalEntityViewSet, IndividualViewSet

router = DefaultRouter()
router.register(r'legal_entity', LegalEntityViewSet, basename='user')
router.register(r'individual', IndividualViewSet, basename='user')

urlpatterns = router.urls