from cloudinary.models import CloudinaryField
from django.db import models
from django.template.defaultfilters import escape
from django.urls import reverse
from django.utils.html import format_html


class Level(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True)
    icon = CloudinaryField(null=False)

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.name


class Subject(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    levels = models.ManyToManyField('Level', through=Level.subjects.through, blank=True)
    chapters = models.ManyToManyField('Chapter', blank=True)
    icon = CloudinaryField(null=False)

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.name

    def subject_link(self):
        return format_html('<a href="%s">%s</a>' % (
            reverse("admin:courses_subject_change", args=(self.subject.id,)), escape(self.subject)))


class Chapter(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', through=Subject.chapters.through, blank=True)

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.name


class Description(models.Model):
    text = models.CharField(max_length=500)
    lesson = models.ForeignKey('Lesson', related_name="descriptions", on_delete=models.CASCADE)

    
class Lesson(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    video = models.FileField()
    chapter = models.ForeignKey('Chapter', related_name="lessons", on_delete=models.CASCADE)
    thumbnail = CloudinaryField(null=False)

    class Meta:
        ordering = ['num']
        
    def chapter_link(self):
        return format_html('<a href="%s">%s</a>' % (
            reverse("admin:courses_chapter_change", args=(self.chapter.id,)), escape(self.chapter)))

    chapter_link.allow_tags = True
    chapter_link.short_description = "Chapter"

    def __str__(self):
        return self.name
