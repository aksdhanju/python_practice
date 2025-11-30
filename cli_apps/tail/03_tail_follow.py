#!/usr/bin/env python3
"""
A Python implementation of `tail -f` (follow mode)
"""

import time
import os

def tail_follow_basic(filepath, sleep_interval=0.5):
    with open(filepath, "r", encoding="utf-8") as f:
        # Move to end of file
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line, end="")  # Already has newline
            else:
                # No new data, wait and retry
                time.sleep(sleep_interval)

def tail_follow(filepath, sleep_interval=0.5):
    with open(filepath, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        last_inode = os.fstat(f.fileno()).st_ino
        while True:
            line = f.readline()
            if line:
                print(line, end="")
                continue
            # If no new line, pause
            time.sleep(sleep_interval)
            try:
                # Check if file was rotated/replaced
                current_inode = os.stat(filepath).st_ino
                if current_inode != last_inode:
                    print("\n[File rotated — switching to new file]\n")
                    f.close()
                    f = open(filepath, "r", encoding="utf-8")
                    last_inode = current_inode
                    continue
            except FileNotFoundError:
                # Log file temporarily unavailable
                time.sleep(sleep_interval)
                continue
            # Detect truncation
            if os.path.getsize(filepath) < f.tell():
                print("\n[File truncated — resetting position]\n")
                f.seek(0)


# def tail_follow(filename, n=10, interval=0.5):
#     """
#     Display the last n lines and then follow the file for new content.
    
#     Args:
#         filename: Path to the file
#         n: Number of last lines to show first (default: 10)
#         interval: Time (seconds) to wait before checking for new data
#     """
#     try:
#         with open(filename, 'r') as file:
#             # Move to last n lines
#             try:
#                 file.seek(0, os.SEEK_END)
#                 file_size = file.tell()
                
#                 # Read backwards in chunks to get last n lines efficiently
#                 offset = min(file_size, 4096)
#                 file.seek(file_size - offset)
#                 lines = file.read().splitlines()
#                 last_lines = lines[-n:]
#             except Exception:
#                 # fallback for tiny files
#                 file.seek(0)
#                 last_lines = file.read().splitlines()[-n:]

#             for line in last_lines:
#                 print(line)

#             # Follow mode: continuously watch for new data
#             while True:
#                 line = file.readline()
#                 if line:
#                     print(line, end="")
#                 else:
#                     time.sleep(interval)

#     except FileNotFoundError:
#         print(f"tail: {filename}: No such file or directory")
#     except PermissionError:
#         print(f"tail: {filename}: Permission denied")
#     except KeyboardInterrupt:
#         print("\nStopped following.")

if __name__ == "__main__":
    file_name = '/Users/aksdhanju/yipit/data/rediscli_aio.py'
    tail_follow(file_name, n=20)
