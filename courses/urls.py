

from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('lessons/', LessonList.as_view()),
    path('levels/', LevelList.as_view()),
    path('levels/<int:pk>/subjects', LevelDetail.as_view()),
    path('levels/<int:pk1>/subjects/<int:pk>/chapters', SubjectDetail.as_view()),
    path('levels/<int:pk1>/subjects/<int:pk2>/chapters/<int:pk>/lessons', ChapterWithLessons.as_view())
]
