from rest_framework.routers import DefaultRouter
router = DefaultRouter()


from .views import HumanRecordViewSet, OrganizationRecordViewSet, NeedHelpPostViewSet, \
                   RespondentViewSet, ReportPostViewSet


router.register(r'human_record', HumanRecordViewSet, basename='user')
router.register(r'organization_record', OrganizationRecordViewSet, basename='user')
router.register(r'need_help_post', NeedHelpPostViewSet, basename='user')
router.register(r'respondent', RespondentViewSet, basename='user')
#router.register(r'news_post', NewsPostViewSet, basename='user')
router.register(r'report_post', ReportPostViewSet, basename='user')

urlpatterns = router.urls


