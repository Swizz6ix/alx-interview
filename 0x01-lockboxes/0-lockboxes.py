#!/usr/bin/python3
"""
Lockboxes that contains many keys
"""


def canUnlockAll(boxes):
    """Keys for the lockboxes"""
    box_len = len(boxes)
    found_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_idx = unseen_boxes.pop()
        if not box_idx or box_idx >= box_len or box_idx < 0:
            continue
        if box_idx not in found_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_idx])
            found_boxes.add(box_idx)
    return box_len == len(found_boxes)
