from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from exam.models import UserExam
from exam.serializers import UserExamSerializer


class UserExamCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserExam.objects.all()
    serializer_class = UserExamSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
