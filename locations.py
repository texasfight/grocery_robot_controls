from __future__ import annotations

from typing import Tuple


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
