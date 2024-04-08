#!/usr/bin/env python

# Imports
import os
import sys


# Main function
def main():
    # Set the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.prod")

    # Try
    try:
        # Import the execute_from_command_line function from the django.core.management module
        from django.core.management import execute_from_command_line

    # Except ImportError
    except ImportError as exc:
        # Raise ImportError
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command line
    execute_from_command_line(sys.argv)


# If the file is run as the main program
if __name__ == "__main__":
    # Run the main function
    main()
