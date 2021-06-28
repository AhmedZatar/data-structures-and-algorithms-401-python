from data_structures_and_algorithms_401_python.Challenges.tree_breadth_first.tree_breadth_first import (Node, BinaryTree,breadth_first)
import pytest



def test_breadth_first_happy_path(prepared_tree):
    assert breadth_first(prepared_tree)==[2,7,5,2,6,9,5,11,4]

def test_breadth_first_expected_failure(prepared_tree):
    prepared_tree.root.right.right.left.right = Node(66)
    assert breadth_first(prepared_tree)!=[2,7,5,2,6,9,5,11,4]

def test_breadth_edge_Case():
    tree = BinaryTree()
    assert breadth_first(tree)==[]




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