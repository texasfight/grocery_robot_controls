from __future__ import annotations

from typing import Tuple

import numpy as np

NORMAL_PATH = {
    1: (2,),
    2: (3,),
    3: (4,),
    4: (5,),
    5: (6, 16),
    6: (7,),
    7: (8,),
    8: (9,),
    9: (10, 11),
    10: (1,),
    11: (12,),
    12: (13,),
    13: (14,),
    14: (15,),
    16: (5, 6)
}

REVERSE_PATH = {
    1: (10,),
    2: (1,),
    3: (2,),
    4: (3,),
    5: (4,),
    6: (5, 16),
    7: (6,),
    8: (7,),
    9: (8,),
    10: (9, 11),
    11: (9, 10),
    12: (11,),
    13: (12,),
    14: (13,),
    15: (14,),
    16: (15,)
}

TAG_GRID = np.array([
    [np.NaN, 10,     np.NaN, 11,     np.NaN],
    [1,      np.NaN, 9,      np.NaN, 12],
    [2,      np.NaN, 8,      np.NaN, 13],
    [3,      np.NaN, 7,      np.NaN, 14],
    [4,      np.NaN, 6,      np.NaN, 15],
    [np.NaN, 5,      np.NaN, 16,     np.NaN]
])


def get_node_location(node_id: int) -> np.array:
    """
    Gives the location of the node as a function of the ID
    """
    return np.hstack(np.where(TAG_GRID == node_id))


class Node:
    """
    Represents the location of the robot in terms of its node, orientation, and target.
    """
    def __init__(self, node_id: int, reverse: bool = False):
        self.id = node_id
        self.location = get_node_location(self.id)
        if reverse:
            targets = REVERSE_PATH[self.id]
        else:
            targets = NORMAL_PATH[self.id]

        if len(targets) == 1:
            self.target_id = targets[0]
            self.target_location = get_node_location(self.target_id)

    def generate_motor_outputs(self) -> (int, int):
        ...


