from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import *


class SubjectInline(admin.TabularInline):
    model = Level.subjects.through
    fields = ['subject_name']
    readonly_fields = ['subject_name']

    def subject_name(self, instance):
        return format_html('<a href="%s">%s</a>' % (
            reverse("admin:courses_subject_change", args=(instance.subject.id,)), escape(instance.subject)))

    subject_name.short_description = 'subject name'


class LevelAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]


admin.site.register(Level, LevelAdmin)


class ChapterInline(admin.TabularInline):
    model = Subject.chapters.through
    fields = ['chapter_name']
    readonly_fields = ['chapter_name']

    def chapter_name(self, instance):
        return format_html('<a href="%s">%s</a>' % (
            reverse("admin:courses_chapter_change", args=(instance.chapter.id,)), escape(instance.chapter)))

    chapter_name.short_description = 'chapter name'


class SubjectAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


admin.site.register(Subject, SubjectAdmin)


class LessonInline(admin.TabularInline):
    model = Lesson


class ChapterAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


admin.site.register(Chapter, ChapterAdmin)


class DescriptionInline(admin.TabularInline):
    model = Description


class LessonAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]

admin.site.register(Lesson, LessonAdmin)
