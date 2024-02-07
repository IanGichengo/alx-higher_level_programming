#!/usr/bin/python3

import sys


def print_metrics(file_sizes, status_codes):
    """
    Print metrics computed from file sizes and status codes.

    Args:
        file_sizes (list): List of file sizes.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size:", sum(file_sizes))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


line_count = 0
file_sizes = []
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        file_size = int(parts[-1])
        file_sizes.append(file_size)
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
        if line_count % 10 == 0:
            print_metrics(file_sizes, status_codes)
except KeyboardInterrupt:
    print_metrics(file_sizes, status_codes)
    raise
