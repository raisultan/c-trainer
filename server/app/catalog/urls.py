from django.urls import path

from catalog.views import CompressorInfoListAPIView

urlpatterns = [
    path('', CompressorInfoListAPIView.as_view(), name='compressor-info-list'),
]
