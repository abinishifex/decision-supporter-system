from django.contrib import admin

from .models import DecisionSession


@admin.register(DecisionSession)
class DecisionSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "recommendation", "created_at")
    search_fields = ("problem", "recommendation", "category_name")
    readonly_fields = ("created_at",)
