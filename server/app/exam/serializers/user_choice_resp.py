from rest_framework import serializers

from exam.models import ChoiceResponse


class UserChoiceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceResponse
        fields = ('base_question', 'user_exam', 'answer_id')
