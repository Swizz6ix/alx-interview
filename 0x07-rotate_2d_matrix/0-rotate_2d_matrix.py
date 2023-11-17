#!/usr/bin/python3
"""This module contains function that rotate 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix) -> None:
    """Rotate 2D matrix by 90 degrees"""
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            # transpose matrix i.e swap elements across
            # main diagonal (x - shaped swapping)
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    for x in range(len(matrix)):
        matrix[x].reverse()
