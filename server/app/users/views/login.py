from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserAuthSerializer


class UserAuthAPIView(TokenObtainPairView):
    serializer_class = UserAuthSerializer
