from rest_framework.generics import ListAPIView

from catalog.serializers import CompressorInfoSerializer
from catalog.models import CompressorInfo


class CompressorInfoListAPIView(ListAPIView):
    serializer_class = CompressorInfoSerializer
    queryset = CompressorInfo.objects.all()
