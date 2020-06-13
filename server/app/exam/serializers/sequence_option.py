from rest_framework import serializers

from exam.models import SequenceOption


class SequenceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenceOption
        fields = ('id', 'title', 'number_in_seq')
