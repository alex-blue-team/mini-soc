"""
detector.py

Simple keyword-based detection module for Mini-SIEM.
Detects suspicious patterns in log lines.
"""

SUSPICIOUS_WORDS = ["failed", "error", "invalid"]


def detect_suspicious(line):
    """
    Check if a log line contains suspicious keywords.

    Args:
        line (str): A single log line.

    Returns:
        bool: True if suspicious keyword is found, False otherwise.
    """
    line_lower = line.lower()

    for word in SUSPICIOUS_WORDS:
        if word in line_lower:
            return True

    return False
