"""
config.py

Central configuration file for the mini-SIEM system.

Contains:
- supported CLI modes
- brute-force detection thresholds
"""

AVAILABLE_MODES = ("--streaming", "--summary", "--both")

# Brute-force detection thresholds (number of failed logins)
CRITICAL_THRESHOLD = 100
HIGH_THRESHOLD = 20
MEDIUM_THRESHOLD = 5