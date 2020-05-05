from rest_framework import serializers

from catalog.models import CompressorInfo


class CompressorInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CompressorInfo
        fields = ('id', 'image', 'title', 'text')

    def get_image(self, obj):
        return obj.image.name
