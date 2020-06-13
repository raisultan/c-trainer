from rest_framework import serializers

from exam.models import Question

from .choice_option import ChoiceOptionSerializer
from .sequence_option import SequenceOptionSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'is_sequence', 'options')

    def get_options(self, obj):
        if obj.is_sequence:
            return SequenceOptionSerializer(obj.sequence.options.all(), many=True).data
        return ChoiceOptionSerializer(obj.choice.options.all(), many=True).data
