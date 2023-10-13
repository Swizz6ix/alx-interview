#!/usr/bin/env python3
"""
a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print ('H', end='')
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 2:
            done += clipboard
            ops_count += 1
    return ops_count