"""
main.py

Application entry point.

Validates command-line arguments and starts
the selected operating mode.
"""

from cli import check_path_and_mode
from runner import start_streaming_mode
from runner import start_summary_mode


def main():

    mode = check_path_and_mode()

    if mode is None:
        return

    streaming_mode = mode in ("--streaming", "--both")
    summary_mode = mode in ("--summary", "--both")

    # Run real-time analysis mode.
    if streaming_mode:
        start_streaming_mode()

    # Run summary analysis mode.
    if summary_mode:
        start_summary_mode()


if __name__ == "__main__":
    main()