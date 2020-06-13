from django.urls import path

from exam.views import ExamListAPIView, ExamRetrieveAPIView

urlpatterns = [
    path('', ExamListAPIView.as_view(), name='exam-list'),
    path('<str:pk>/', ExamRetrieveAPIView.as_view(), name='exam-detail'),
]
