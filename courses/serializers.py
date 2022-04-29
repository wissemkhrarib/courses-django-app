from rest_framework import serializers

from .models import Lesson, Subject, Level, Chapter, Description


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name', 'icon']


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ['id', 'name', 'subjects']
        depth = 2


class LessonDetailSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=False, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name','num', 'video', 'thumbnail', 'chapter']


class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = ['id', 'text']


class LessonSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video', 'descriptions']


class ChapterWithLessonsSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'name', 'lessons']


class SubjectWithChaptersSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'icon', 'chapters']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'name', 'icon']


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['id', 'name', 'icon']


class LevelWithSubjectsSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ['id', 'name', 'icon', 'subjects']
