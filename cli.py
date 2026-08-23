import os
import sys

import config


def take_file_path():

    file_path = sys.argv[1]

    return file_path


def check_path_and_mode():

    if len(sys.argv) < 3:

        _suggest_input_method()
        return None

    file_path = take_file_path()

    if not os.path.exists(file_path):

        print(
            "\nError",
            f"\nInvalid path specified: {file_path}\n"
        )
        return None

    if len(sys.argv) > 3:

        print(
            "\nToo many arguments specified\n",
            "\nSee the specification\n"
        )
        return None

    mode = sys.argv[2]

    if mode not in config.AVAILABLE_MODES:

        _suggest_input_mode(mode)
        return None

    return mode


def _suggest_input_method():

    print(
        "\nError",
        "\nSpecify the file path and operating mode.\n",
        "\nAvailable modes:",
        "\n  --streaming",
        "\n  --summary",
        "\n  --both\n"
    )


def _suggest_input_mode(mode):

    print(
        "\nError",
        f"\nInvalid mode specified {mode.upper()}\n",
        "\nAvailable modes:",
        "\n  --streaming",
        "\n  --summary",
        "\n  --both\n"
    )