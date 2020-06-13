from django.urls import path

from exam.views import ExamListAPIView

urlpatterns = [
    path('', ExamListAPIView.as_view(), name='exam-list'),
]
