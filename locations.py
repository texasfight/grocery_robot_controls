from __future__ import annotations

from typing import Tuple

import numpy as np

NORMAL_DICT = {
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

REVERSE_DICT = {
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

class Linkage:
    def __init__(self, node1: Node, node2: Node):
        ...


class Node:
    def __init__(self, node_id: int, linkages: Tuple[Linkage]):
        self.id = node_id
        if linkages:
            self.linkages = linkages
        else:
            self.linkages = tuple()

    def add_linkage(self, linkage: Linkage):
        self.linkages += linkage

    def update_id(self, new_id: int):
        self.id = new_id
