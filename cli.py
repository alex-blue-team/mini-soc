# Handles command-line arguments:
# - validates input parameters
# - checks file existence
# - verifies selected operating mode

import sys
import os


AVAILABLE_MODES = ("--streaming", "--summary", "--both")


def indicate_correct_input():
    # Display usage information when arguments are missing.
    print("\nError",
        "\nSpecify the correct path and mode\n",
        "\nAvailable modes:",
        "\n --streaming",
        "\n --summary",
        "\n --both\n")


def suggest_correct_mode(mode):
    # Display available modes when an invalid mode is specified.
    print("\nError",
        f"\nIncorrect mode specified: {mode.upper()}\n",
        "\nAvailable modes:",
        "\n --streaming",
        "\n --summary",
        "\n --both\n"
        )


def validate_cli_arguments():
    # Validate command-line arguments before program execution.

    if len(sys.argv) < 3:
        indicate_correct_input()
        return None

    file_path = get_file_path()

    if not os.path.exists(file_path):
        print("\nError",
            f"\nA non-existent path was specified: {file_path}\n")
        return None

    mode = sys.argv[2]

    if len(sys.argv) > 3:
        print("\nToo many arguments\n",
            "\nSee specification\n")
        return None

    if mode not in AVAILABLE_MODES:
        suggest_correct_mode(mode)
        return None

    return mode


def get_file_path():
    # Return the log file path provided by the user.

    file_path = sys.argv[1]

    return file_path