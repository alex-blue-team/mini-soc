import config

from cli import check_path_and_mode
from runner import start_streaming_mode
from runner import start_summary_mode


def main():

    mode = check_path_and_mode()

    if mode in config.STREAMING_MODES:
        start_streaming_mode()

    if mode in config.SUMMARY_MODES:
        start_summary_mode()


if __name__ == "__main__":
    main()