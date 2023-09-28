#!/usr/bin/python3
"""
function that returns a list of lists of integers representing the Pascal’s triangle of n 
"""

def pascal_triangle(n):
    """
    Presentation of the pascal triangle
    """
    result = []

    if n <= 0:
        return []
    
    for row in range(n):
        new_row = [1]

        for col in range(1, row+1):
            new_Cell = new_row[col-1] * float(row+1-col)/col
            new_row.append(int(new_Cell))

        result.append(new_row)

    return result