from rest_framework import serializers

from exam.models import ChoiceOption


class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = ('id', 'title', 'is_correct')
