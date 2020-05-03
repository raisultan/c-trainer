from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserAuthAPIView

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('login/', UserAuthAPIView.as_view(), name='login'),
]
