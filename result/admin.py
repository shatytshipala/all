# pylint: disable-all
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import TakenCourse, Result


class ScoreAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "course",
        "assignment",
        "mid_exam",
        "quiz",
        "attendance",
        "marks_1",
        "marks_2",
        "marks_3",
        "marks_4",
        "final_exam",
        "total",
        "grade",
        "comment",
    ]


admin.site.register(TakenCourse, ScoreAdmin)
admin.site.register(Result)
