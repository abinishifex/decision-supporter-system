from django.contrib import admin
from .models import DecisionSession, Category, Question, AllowedAnswer

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(AllowedAnswer)

@admin.register(DecisionSession)
class DecisionSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "problem", "category", "recommendation", "created_at")
    search_fields = ("problem", "recommendation")
    readonly_fields = ("created_at",)
