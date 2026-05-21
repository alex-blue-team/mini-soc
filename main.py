import json
from parser import read_log
from alert import create_alert
from correlator import count_events


def main():

    # Switch log samples manually
    #file_path = "test_01.log"
    #file_path = "test_02.log"
    file_path = "test_03.log"

    # Read log file line by line
    for line in read_log(file_path):

        result = count_events(line)

        # Print alert if threat detected
        if result:
            create_alert(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
