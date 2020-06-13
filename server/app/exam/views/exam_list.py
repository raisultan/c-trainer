from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from exam.models import Exam
from exam.serializers import ExamListSerializer


class ExamListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer
