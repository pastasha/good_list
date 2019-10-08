from rest_framework import viewsets

from .models import LegalEntity, Individual
from .serializers import LegalEntitySerializer, IndividualSerializer


class LegalEntityViewSet(viewsets.ModelViewSet):
    serializer_class = LegalEntitySerializer
    queryset = LegalEntity.objects.all()


class IndividualViewSet(viewsets.ModelViewSet):
    serializer_class = IndividualSerializer
    queryset = Individual.objects.all()