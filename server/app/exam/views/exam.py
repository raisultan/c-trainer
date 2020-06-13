from rest_framework.generics import RetrieveAPIView

from exam.models import Exam
from exam.serializers import ExamSerializer


class ExamRetrieveAPIView(RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
