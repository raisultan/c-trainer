from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import StudentAuthSerializer


class StudentAuthAPIView(TokenObtainPairView):
    serializer_class = StudentAuthSerializer
