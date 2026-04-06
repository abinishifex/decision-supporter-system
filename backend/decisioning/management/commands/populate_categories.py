from django.core.management.base import BaseCommand
from decisioning.models import Category

class Command(BaseCommand):
    help = 'Populate initial categories for the decisioning app'

    def handle(self, *args, **kwargs):
        categories = [
            {"name": "Career", "icon": "💼", "description": "Job choice, career path, switching fields"},
            {"name": "Education", "icon": "📚", "description": "Courses, learning paths, skills"},
            {"name": "Business", "icon": "🚀", "description": "Starting a business, scaling, partnerships"},
            {"name": "Relationships", "icon": "❤️", "description": "Friends, partners, social decisions"},
            {"name": "Family", "icon": "👨👩👧", "description": "Family responsibilities, personal life choices"},
            {"name": "Health", "icon": "🏃♂️", "description": "Fitness, diet, medical-related decisions"},
            {"name": "Lifestyle", "icon": "🌍", "description": "Daily habits, living choices, routines"},
            {"name": "Technology", "icon": "💻", "description": "Choosing tools, software, devices"},
            {"name": "Personal Growth", "icon": "🌱", "description": "Self-improvement, mindset, discipline"},
        ]

        for cat_data in categories:
            obj, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={
                    "icon": cat_data["icon"],
                    "description": cat_data["description"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created category "{cat_data["name"]}"'))
            else:
                # Update icon and description if they changed
                obj.icon = cat_data["icon"]
                obj.description = cat_data["description"]
                obj.save()
                self.stdout.write(self.style.NOTICE(f'Updated category "{cat_data["name"]}"'))
