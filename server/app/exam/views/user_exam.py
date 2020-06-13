from rest_framework.generics import CreateAPIView

from exam.models import UserExam
from exam.serializers import UserExamSerializer


class UserExamCreateAPIView(CreateAPIView):
    queryset = UserExam.objects.all()
    serializer_class = UserExamSerializer
