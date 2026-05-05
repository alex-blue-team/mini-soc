"""
test_parser.py

Simple test script for parser.py.
Prints log lines to verify parser functionality.
"""

from parser import read_log
from detector import detect_suspicious

def main():
    file_path = "test.log"

    for line in read_log(file_path):
    	if detect_suspicious(line):
        	print("[ALERT]", line)
    	else:
	        print(line)


if __name__ == "__main__":
    main()
