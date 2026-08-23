import json

from cli import take_file_path
from parser import read_logs
from correlator import BruteForceDetector
from alert import create_alert


def start_streaming_mode():

    file_path = take_file_path()

    detector = BruteForceDetector()

    for log_line in read_logs(file_path):

        alert = detector.process_event(log_line)

        if alert:
            create_alert(json.dumps(alert, indent=4))


def start_summary_mode():

    file_path = take_file_path()

    detector = BruteForceDetector()

    alerts = detector.process_events(
        read_logs(file_path)
    )

    for alert in alerts:
        create_alert(json.dumps(alert, indent=4))