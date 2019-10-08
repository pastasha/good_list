from rest_framework.routers import DefaultRouter

from .views import LegalEntityViewSet, IndividualViewSet

router = DefaultRouter()
router.register(r'good_api/legal_entity', LegalEntityViewSet, basename='user')
router.register(r'good_api/individual', IndividualViewSet, basename='user')

urlpatterns = router.urls