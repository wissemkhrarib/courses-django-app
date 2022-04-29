from rest_framework import generics

from .pagination.pagination import LargeResultsSetPagination
from .serializers import LevelSerializer, LevelWithSubjectsSerializer, SubjectWithChaptersSerializer, \
    ChapterWithLessonsSerializer, LessonSerializer, LessonDetailSerializer
from .models import Level, Subject, Chapter, Lesson


class ChapterWithLessons(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterWithLessonsSerializer


class LevelList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetail(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelWithSubjectsSerializer


class SubjectDetail(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectWithChaptersSerializer


class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    pagination_class = LargeResultsSetPagination
