from rest_framework import serializers

from .models import LegalEntity, Individual

class LegalEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntity
        fields = ('id', 'name', 'description')

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ('id', 'name', 'description')