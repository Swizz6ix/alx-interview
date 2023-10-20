#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    # No operation has been file_text yet
    ops_count = 0
    # Assume nothing has been copied to the clipboard yet
    clipboard = 0
    # Assume the file contain 1 alphabet (H)
    file_text = 1
    # print ('H', end='')
    while file_text < n:
        # copy all when the length is divisible by n
        if n % file_text == 0:
            clipboard = file_text
            ops_count += 1
        # paste all the time. Action 2
        file_text += clipboard
        ops_count += 1
    return ops_count
