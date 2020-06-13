from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from exam.views import UserExamCreateAPIView, UserChoiceResponseCreateAPIView, UserSequenceResponseCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/exams/', include('exam.urls')),
    path('api/user-exam/', UserExamCreateAPIView.as_view(), name='user-exam-create'),
    path('api/user-exam/choice/', UserChoiceResponseCreateAPIView.as_view(), name='user-choice-create'),
    path('api/user-exam/sequence/', UserSequenceResponseCreateAPIView.as_view(), name='user-sequence-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
