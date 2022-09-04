from django.contrib import admin

# Register your models here.
from courseapp import models
from courseapp.models import Homework, HomeworkQuestion, Quiz, QuizQuestion, Chapter, Title, ChapterTitles


class ChapterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chapter, ChapterAdmin)


class TitleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Title, TitleAdmin)


class ChapterTitlesAdmin(admin.ModelAdmin):
    pass


admin.site.register(ChapterTitles, ChapterTitlesAdmin)


class HomeworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Homework, HomeworkAdmin)


class HomeworkQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(HomeworkQuestion, HomeworkQuestionAdmin)


class QuizAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)


class QuizQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(QuizQuestion, QuizQuestionAdmin)
