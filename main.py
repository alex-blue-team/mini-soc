# Entry point of the mini-SIEM.
# Validates user input and starts the selected processing mode.

from cli import validate_cli_arguments
from runner import start_streaming_mode
from runner import start_summary_mode


def main():

	# Validate command-line arguments.
	result = validate_cli_arguments()

	if result is None:
		return

	mode = result

	# Determine which operating modes should be executed.
	is_streaming_enabled = mode in ("--streaming", "--both")
	is_summary_enabled = mode in ("--summary", "--both")

	if is_streaming_enabled:
		start_streaming_mode()

	if is_summary_enabled:
		start_summary_mode()


if __name__ == "__main__":
	# Start the application.
	main()