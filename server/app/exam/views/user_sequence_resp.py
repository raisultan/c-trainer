from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exam.models import Sequence, SequenceResponse
from exam.serializers import UserSequenceResponseSerializer


class UserSequenceResponseCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SequenceResponse.objects.all()
    serializer_class = UserSequenceResponseSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        option = Sequence.objects.get(
            id=response.data['base_question']
        ).options.get(
            title=response.data['title']
        )

        return Response({
            'is_correct': option.number_in_seq == response.data['number_in_seq'],
            'data': response.data
        }, status=status.HTTP_201_CREATED)
