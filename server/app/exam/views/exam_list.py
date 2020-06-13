from rest_framework.generics import ListAPIView

from exam.models import Exam
from exam.serializers import ExamListSerializer


class ExamListAPIView(ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer
