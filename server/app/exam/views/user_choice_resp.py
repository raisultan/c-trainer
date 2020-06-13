from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exam.models import Choice, ChoiceResponse
from exam.serializers import UserChoiceResponseSerializer


class UserChoiceResponseCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ChoiceResponse.objects.all()
    serializer_class = UserChoiceResponseSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        correct_option = Choice.objects.get(
            id=response.data['base_question']
        ).options.filter(
            is_correct=True
        ).first()

        return Response({
            'is_correct': correct_option.id == response.data['answer_id'],
            'data': response.data
        }, status=status.HTTP_201_CREATED)
