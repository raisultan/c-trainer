from rest_framework import serializers

from exam.models import Exam


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'max_time', 'questions_count')
