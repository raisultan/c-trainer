from rest_framework import serializers

from exam.models import Question

from .choice_option import ChoiceOptionSerializer
from .sequence_option import SequenceOptionSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    related_question_id = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'related_question_id', 'title', 'is_sequence', 'options')

    def get_options(self, obj):
        if obj.is_sequence:
            return SequenceOptionSerializer(obj.sequence.options.all(), many=True).data
        return ChoiceOptionSerializer(obj.choice.options.all(), many=True).data

    def get_related_question_id(self, obj):
        if obj.is_sequence:
            return obj.sequence.id
        return obj.choice.id
