# Main entry point of the mini SIEM system.
# Reads logs, analyzes events, and creates alerts.

from parser import read_log
from correlator import count_events
from alert import create_alert


def main():
    # Path to the log file
    file_path = "test.log"

    # Read log file line by line
    for line in read_log(file_path):

        # Analyze events in logs
        result = count_events(line)

        # Create alert if suspicious activity detected
        if result:
            create_alert(result)


# Run program directly from terminal
if __name__ == "__main__":
    main()
