#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a script that reads stdin
line by line and computes metrics:"""
import sys
import signal

# Initialize variables to hold the total file size and
# the count of each status code
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
line_count = 0


def print_statistics():
    """Print the accumulated statistics."""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signum, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)


# Register the interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        # Extract the file size and status code from the line
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Accumulate the file size
        total_file_size += file_size

        # Increment the status code count if it's one of the specified codes
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    print(f"An error occurred: {e}")

# Print final statistics if the script ends normally
print_statistics()
