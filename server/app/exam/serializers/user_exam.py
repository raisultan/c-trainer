from rest_framework import serializers

from exam.models import UserExam
from users.models import BaseUser


class UserExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExam
        fields = ('id', 'base_exam', 'user', 'time_spent')
        read_only_fields = ('id', 'user')
