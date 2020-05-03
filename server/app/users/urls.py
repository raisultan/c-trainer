from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import StudentAuthAPIView

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('student/', StudentAuthAPIView.as_view(), name='student-auth'),
]
