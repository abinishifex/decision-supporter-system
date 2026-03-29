#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path


def maybe_rerun_with_local_venv():
    current_executable = Path(sys.executable).resolve()
    repo_root = Path(__file__).resolve().parent.parent
    venv_python = repo_root / "djangoenv" / "Scripts" / "python.exe"

    if not venv_python.exists():
        return False

    if current_executable == venv_python.resolve():
        return False

    completed = subprocess.run([str(venv_python), *sys.argv], check=False)
    raise SystemExit(completed.returncode)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        if exc.name == "django":
            maybe_rerun_with_local_venv()
        raise ImportError(
            "Couldn't import Django. Activate the local virtualenv with "
            "'djangoenv\\Scripts\\Activate.ps1' or run commands with "
            "'djangoenv\\Scripts\\python.exe backend\\manage.py ...'."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
