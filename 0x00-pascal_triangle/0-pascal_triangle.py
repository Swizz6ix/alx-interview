#!/usr/bin/python3
"""
function that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Presentation of the pascal triangle
    """
    result = []

    if n <= 0:
        return []

    for row in range(n):
        new_row = []

        for col in range(row + 1):
            if col == 0 or col == row:
                new_row.append(1)
            else:
                prevRow = result[row - 1]
                new_row.append(prevRow[col] + prevRow[col - 1])
        result.append(new_row)
    return result
