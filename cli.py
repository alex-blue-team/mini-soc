"""
cli.py

Handles command-line arguments for the mini-SIEM system.

Validates:
- input file path
- selected operating mode
"""

import sys
import os

import config


def take_file_path():
    """Get file path from command-line arguments."""

    # First CLI argument is the file path
    file_path = sys.argv[1]
    return file_path


def check_path_and_mode():
    """Validate CLI arguments and return selected mode."""

    # We expect: script.py <file_path> <mode>
    if len(sys.argv) < 3:
        _suggest_input_method()
        return None

    file_path = take_file_path()

    # Check that file exists before processing
    if not os.path.exists(file_path):
        print("\nError",
              f"\nInvalid path specified: {file_path}\n")
        return None

    # Ensure no extra arguments were passed
    if len(sys.argv) > 3:
        print("\nToo many arguments specified\n",
              "\nSee the specification\n")
        return None

    mode = sys.argv[2]

    # Validate selected mode against config
    if mode not in config.AVAILABLE_MODES:
        _suggest_input_mode(mode)
        return None

    return mode


def _suggest_input_method():
    """Show correct usage of the CLI."""

    print("\nError",
          "\nSpecify the file path and operating mode.\n",
          "\nAvailable modes:",
          "\n  --streaming",
          "\n  --summary",
          "\n  --both\n")


def _suggest_input_mode(mode):
    """Show error and list valid modes."""

    print("\nError",
          f"\nInvalid mode specified {mode.upper()}\n",
          "\nAvailable modes:",
          "\n  --streaming",
          "\n  --summary",
          "\n  --both\n")