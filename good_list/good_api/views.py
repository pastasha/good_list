from rest_framework import viewsets


from .models import HumanRecord, OrganizationRecord, NeedHelpPost, Respondent, ReportPost
from .serializers import HumanRecordSerializer, OrganizationRecordSerializer, NeedHelpPostSerializer, \
                         RespondentSerializer, ReportPostSerializer

class HumanRecordViewSet(viewsets.ModelViewSet):
    serializer_class = HumanRecordSerializer
    queryset = HumanRecord.objects.all()

class OrganizationRecordViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationRecordSerializer
    queryset = OrganizationRecord.objects.all()

class NeedHelpPostViewSet(viewsets.ModelViewSet):
    serializer_class = NeedHelpPostSerializer
    queryset = NeedHelpPost.objects.all()

class RespondentViewSet(viewsets.ModelViewSet):
    serializer_class = RespondentSerializer
    queryset = Respondent.objects.all()

'''
class NewsPostViewSet(viewsets.ModelViewSet):
    serializer_class = NewsPostSerializer
    queryset = NewsPost.objects.all()
'''

class ReportPostViewSet(viewsets.ModelViewSet):
    serializer_class = ReportPostSerializer
    queryset = ReportPost.objects.all()
