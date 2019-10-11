from rest_framework import serializers

from .models import HumanRecord, OrganizationRecord, NeedHelpPost, Respondent, ReportPost

'''
class GoodDeedAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodDeedAbstract
        fields = ('id', 'STATUS_DISTURBANCES', 'first_name', 'second_name', 'last_name', 'email', 'phone_number',
                  'problem_description', 'adres', 'file', 'date_added', 'status')

class PostAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAbstract
        fields = ('id', 'title', 'short_description', 'full_description', 'published_date', 'image')
'''

class HumanRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanRecord
        fields = ('id', 'STATUS_DISTURBANCES', 'first_name', 'second_name', 'last_name', 'email', 'phone_number',
                  'problem_description', 'adres', 'file', 'date_added', 'status', 'LIST_NEEDED_HELP', 'birthday', 'type_needed_help')

class OrganizationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationRecord
        fields = ('id', 'STATUS_DISTURBANCES', 'first_name', 'second_name', 'last_name', 'email', 'phone_number',
                  'problem_description', 'adres', 'file', 'date_added', 'status', 'organization_name', 'info_about_organization', 'special_code')

class NeedHelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedHelpPost
        fields = ('id', 'title', 'short_description', 'full_description', 'published_date', 'image', 'organization_request', 'human_request')

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondent
        fields = ('id', 'linked_post', 'email', 'number')

'''
class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ('id', 'linked_post', 'email', 'number')
'''

class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportPost
        fields = ('id', 'organization_request', 'human_request')
