#!/usr/bin/env python3
"""
A Python implementation of tail -c <bytes>
"""

def tail_bytes(filename, n):
    """
    Display the last n bytes of a file
    
    Args:
        filename: Path to the file
        n: Number of bytes to display
    """
    try:
        with open(filename, 'rb') as file:
            file.seek(0, 2)          # Move cursor to end
            file_size = file.tell()
            
            # If file shorter than n bytes, read from beginning
            start = max(file_size - n, 0)
            file.seek(start)

            data = file.read()
            try:
                # Print decoding safely if text
                print(data.decode(errors="replace"), end="")
            except UnicodeDecodeError:
                # Show raw bytes if binary
                print(data)
    except FileNotFoundError:
        print(f"tail: {filename}: No such file or directory")
    except PermissionError:
        print(f"tail: {filename}: Permission denied")


# Test
if __name__ == "__main__":
    file_name = '/Users/aksdhanju/yipit/data/rediscli_aio.py'
    tail_bytes(file_name, 100)  # last 100 bytes
