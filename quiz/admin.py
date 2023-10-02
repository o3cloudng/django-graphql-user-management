from django.contrib import admin
from .models import *


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Quizes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
class AnswerInLineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
    ]
    inlines = [
        AnswerInLineModel,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # model = Answer
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]
