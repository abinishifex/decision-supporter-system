from django.contrib import admin
from .models import Category, Question, AllowedAnswer, DecisionSession

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "icon", "created_at")
    search_fields = ("name", "description")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "category", "order")
    list_filter = ("category",)
    search_fields = ("text",)


@admin.register(AllowedAnswer)
class AllowedAnswerAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "question")
    list_filter = ("question",)
    search_fields = ("label",)


@admin.register(DecisionSession)
class DecisionSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "problem", "category", "status", "recommendation", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("problem", "recommendation")
    readonly_fields = ("created_at",)
