#!/usr/bin/env python3
"""
A Python implementation of the tail command
"""

def tail_basic(filename, n=10):
    """
    Display the last n lines of a file
    
    Args:
        filename: Path to the file
        n: Number of lines to display (default: 10)
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Get last n lines
            last_lines = lines[-n:]
            
            for line in last_lines:
                print(line, end='')       
    except FileNotFoundError:
        print(f"tail: {filename}: No such file or directory")
    except PermissionError:
        print(f"tail: {filename}: Permission denied")

# Test the function
if __name__ == "__main__":
    file_name = '/Users/aksdhanju/yipit/data/rediscli_aio.py'
    tail_basic(file_name, 5)