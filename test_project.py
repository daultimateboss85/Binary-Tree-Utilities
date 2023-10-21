import pytest
from project import Node, get_max_depth, get_nodes_bylevel, inorder_traversal

def test_instantiation():
    node = Node("a")