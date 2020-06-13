from rest_framework import serializers

from exam.models import Exam
from .question import QuestionSerializer


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'max_time', 'questions_count')


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'max_time', 'questions_count', 'questions')
