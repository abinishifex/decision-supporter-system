import re

with open('backend/config/settings.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = """import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

STATIC_ROOT = BASE_DIR / "staticfiles"
"""

new_content = re.sub(r'DATABASES = \{.*?\}', replacement, content, flags=re.DOTALL)

with open('backend/config/settings.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
