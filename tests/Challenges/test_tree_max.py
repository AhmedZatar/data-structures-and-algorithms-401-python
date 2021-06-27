from data_structures_and_algorithms_401_python.Challenges.tree_max.tree_max import (Node, BinaryTree,)
import pytest



def test_max_happy_path(prepared_tree):
    assert prepared_tree.max()==11

def test_max_expected_failure(prepared_tree):
    assert prepared_tree.max()!=9

def test_edge_Case(prepared_tree):
    prepared_tree.root.left.right = Node('Ahmed')
    assert prepared_tree.max()=='All tree input should be numbers'

@pytest.fixture
def prepared_tree():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)

    return tree