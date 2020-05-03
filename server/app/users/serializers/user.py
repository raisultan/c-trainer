from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserAuthSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'Неверный логин или пароль',
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if self.user.is_trainer:
            raise serializers.ValidationError('Пользователь не является студентом')

        return {
            'username': self.user.username,
            'tokens': {
                'refresh': validated_data['refresh'],
                'access': validated_data['access'],
            },
            'role': self.user.role,
        }
