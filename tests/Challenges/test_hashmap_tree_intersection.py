import pytest
from data_structures_and_algorithms_401_python.Challenges.hashmap_tree_intersection.hashmap_tree_intersection import *


def test_happy_path(prepared_tree1,prepared_tree2):

    actual=intersection(prepared_tree1,prepared_tree2)
    expected=[100, 160, 125, 175, 200, 350, 500] 
    assert actual==expected



def test_edge_case():
    tree1=BinaryTree()
    tree2=BinaryTree()
    actual=intersection(tree1,tree2)
    expected='one of the tree is empty'
    
    assert actual==expected


def test_expected_failure(prepared_tree1,prepared_tree2):
    prepared_tree1.root.left=Nodet(600)
    actual=intersection(prepared_tree1,prepared_tree2)
    expected=[100, 160, 125, 175, 200, 350, 500] 
    assert actual!=expected


@pytest.fixture
def prepared_tree1():
    tree1=BinaryTree()
    tree1.root=Nodet(150)
    tree1.root.left=Nodet(100)
    tree1.root.right=Nodet(250)
    tree1.root.left.left=Nodet(75)
    tree1.root.left.right=Nodet(160)
    tree1.root.right.left=Nodet(200)
    tree1.root.right.right=Nodet(350)
    tree1.root.left.right.left=Nodet(125)
    tree1.root.left.right.right=Nodet(175)
    tree1.root.right.right.left=Nodet(300)
    tree1.root.right.right.right=Nodet(500)
    return tree1

@pytest.fixture
def prepared_tree2():
    tree2=BinaryTree()
    tree2.root=Nodet(42)
    tree2.root.left=Nodet(100)
    tree2.root.right=Nodet(600)
    tree2.root.left.left=Nodet(15)
    tree2.root.left.right=Nodet(160)
    tree2.root.right.left=Nodet(200)
    tree2.root.right.right=Nodet(350)
    tree2.root.left.right.left=Nodet(125)
    tree2.root.left.right.right=Nodet(175)
    tree2.root.right.right.left=Nodet(4)
    tree2.root.right.right.right=Nodet(500)
    return tree2