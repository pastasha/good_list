from rest_framework.routers import DefaultRouter
router = DefaultRouter()


from .views import HumanRecordViewSet, OrganizationRecordViewSet, NeedHelpPostViewSet, \
                   RespondentViewSet, ReportPostViewSet


router.register(r'human_record', HumanRecordViewSet, basename='1')
router.register(r'organization_record', OrganizationRecordViewSet, basename='2')
router.register(r'need_help_post', NeedHelpPostViewSet, basename='3')
router.register(r'respondent', RespondentViewSet, basename='4')
#router.register(r'news_post', NewsPostViewSet, basename='user')
router.register(r'report_post', ReportPostViewSet, basename='5')

urlpatterns = router.urls


