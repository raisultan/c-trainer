from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from catalog.serializers import CompressorInfoSerializer
from catalog.models import CompressorInfo


class CompressorInfoViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompressorInfoSerializer
    queryset = CompressorInfo.objects.all()
