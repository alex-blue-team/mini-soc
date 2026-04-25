"""
parser.py

Simple log reader for Mini-SIEM project.
"""

def read_log(file_path):
    """Yield log file lines one by one."""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line
