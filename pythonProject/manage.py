import os
import sys


def main():
    """Main function for running administrative tasks."""

    # Set the Django settings module to 'pythonProject.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythonProject.settings')

    try:
        # Try to import the execute_from_command_line function from Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed, raise an ImportError with an informative message
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH. Did you forget to activate a virtual environment?"
        ) from exc

    # Execute Django management commands from the command line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If this script is executed directly, call the main function
    main()
