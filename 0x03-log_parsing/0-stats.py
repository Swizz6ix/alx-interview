#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
"""
from sys import stdin
from typing import Dict


def print_logs(file_size: int, res_dic: Dict[str, int]) -> None:
    """
    Print the log metrics
    """
    print('File size: {}'.format(file_size))
    for key, value in sorted(res_dic.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

line_num = 0
total_file_size = 0
status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
try:
    for line in stdin:
        if line_num != 0 and line_num % 10 == 0:
            print_logs(total_file_size, status_codes_stats)
        line_num += 1
        line_arr = line.split()
        try:
            total_file_size += int(line_arr[-1])
        except Exception:
            pass
        try:
            key = line_arr[-2]
            if key in status_codes_stats:
                status_codes_stats[key] += 1
        except Exception:
            pass
    print_logs(total_file_size, status_codes_stats)
except (KeyboardInterrupt, EOFError):
    print_logs(total_file_size, status_codes_stats)
    raise
