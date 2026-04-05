from django.contrib import admin
from .models import DecisionSession, Category, Question, AllowedAnswer

# Register standard models
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(AllowedAnswer)

@admin.register(DecisionSession)
class DecisionSessionAdmin(admin.ModelAdmin):
    # Added 'status' and replaced analysis with the summary for a better overview
    list_display = ("id", "user", "problem", "category_name", "recommendation", "status", "created_at")
    
    # Allows you to search through the new analysis fields in the admin search bar
    search_fields = ("problem", "recommendation", "analysis_summary", "analysis_pros")
    
    # Keep these as read-only so they can't be accidentally changed in the admin
    readonly_fields = ("created_at", "results", "analysis_summary", "analysis_pros", "analysis_cons")
    
    # Allows you to filter history by status or date in the sidebar
    list_filter = ("status", "created_at", "category_name")