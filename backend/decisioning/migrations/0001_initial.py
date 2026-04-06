from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DecisionSession",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("problem", models.TextField()),
                ("category_id", models.CharField(max_length=100)),
                ("category_name", models.CharField(max_length=255)),
                ("category_payload", models.JSONField()),
                ("options", models.JSONField()),
                ("answers", models.JSONField()),
                ("results", models.JSONField()),
                ("recommendation", models.CharField(max_length=255)),
                ("analysis", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
