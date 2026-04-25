"""
test_parser.py

Simple test script for parser.py.
Prints log lines to verify parser functionality.
"""

from parser import read_log


def main():
    file_path = "test.log"

    for line in read_log(file_path):
        print(line.strip())


if __name__ == "__main__":
    main()
