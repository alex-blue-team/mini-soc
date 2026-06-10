"""
Mini SIEM - Command Line Arguments

This module validates user input received from the terminal:
- checks the number of arguments
- verifies file existence
- validates operating mode
- returns parsed arguments to the application
"""

import sys
import os


AVAILABLE_MODES = ["--streaming", "--summary", "--both"]


def prompt_input_arguments():
    """Display usage information when arguments are missing."""

    print(
        "\nError",
        "\nPlease specify correct path to the file and operating mode\n",
        "\nAvailable modes:",
        "\n --streaming",
        "\n --summary",
        "\n --both\n"
    )


def show_operating_modes(mode):
    """Display available modes when an invalid mode is specified."""

    print(
        "\nError",
        f"\n Incorrect mode specified: {mode.upper()}\n",
        "\nAvailable modes:",
        "\n --streaming",
        "\n --summary",
        "\n --both\n"
    )


def parse_arguments():

    # Validate number of arguments
    if len(sys.argv) < 3:
        prompt_input_arguments()
        return None

    if len(sys.argv) > 3:
        print("\nToo many arguments\n")
        print("\nSee specification\n")
        return None

    file_path = sys.argv[1]
    mode = sys.argv[2]

    # Verify that the log file exists
    if not os.path.exists(file_path):
        print(f"\nFile not found: {file_path}\n")
        print("\nSee specification\n")
        return None

    # Validate selected operating mode
    if mode not in AVAILABLE_MODES:
        show_operating_modes(mode)
        return None

    return file_path, mode