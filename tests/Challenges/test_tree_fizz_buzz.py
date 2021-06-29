from data_structures_and_algorithms_401_python.Challenges.tree_fizz_buzz.tree_fizz_buzz import (KAryTree, Node,fizz_buzz_tree)
import pytest



def test_tree_fizz_buzz_happy_path(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert prepared_kAryTree.root.children[1].value=='Fizz'
    assert prepared_kAryTree.root.children[2].children[1].children[2].value=='Fizz Buzz'


def test_tree_fizz_buzz_expected_failure(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert prepared_kAryTree.root.children[2].children[1].value!='fizz'

def test_tree_fizz_buzz_Case(prepared_kAryTree):
    fizz_buzz_tree(prepared_kAryTree)
    assert type(prepared_kAryTree.root.value) ==type('string') 


@pytest.fixture
def prepared_kAryTree():
    kAryTree = KAryTree()
    kAryTree.root=Node(1)
    kAryTree.root.children+=[Node(2)]
    kAryTree.root.children+=[Node(3)]
    kAryTree.root.children+=[Node(4)]
    kAryTree.root.children[0].children+=[Node(5)]
    kAryTree.root.children[0].children+=[Node(6)]
    kAryTree.root.children[0].children+=[Node(7)]
    kAryTree.root.children[1].children+=[Node(8)]
    kAryTree.root.children[2].children+=[Node(9)]
    kAryTree.root.children[2].children+=[Node(10)]
    kAryTree.root.children[0].children[2].children+=[Node(11)]
    kAryTree.root.children[0].children[2].children+=[Node(12)]
    kAryTree.root.children[2].children[1].children+=[Node(13)]
    kAryTree.root.children[2].children[1].children+=[Node(14)]
    kAryTree.root.children[2].children[1].children+=[Node(15)]
    kAryTree.root.children[2].children[1].children+=[Node(16)]

    return kAryTree