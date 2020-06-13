from rest_framework import serializers

from exam.models import SequenceResponse


class UserSequenceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenceResponse
        fields = ('base_question', 'user_exam', 'title', 'number_in_seq')
