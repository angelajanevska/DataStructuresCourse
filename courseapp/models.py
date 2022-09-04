from django.db import models

# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length=200)


class Title(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)


class ChapterTitles(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)


class Homework(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    isDone = models.BooleanField


class HomeworkQuestion(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    answers = models.TextField(null=True, blank=True)


class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    isDone = models.BooleanField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)


class QuizQuestion(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    answers = models.TextField(null=True, blank=True)


