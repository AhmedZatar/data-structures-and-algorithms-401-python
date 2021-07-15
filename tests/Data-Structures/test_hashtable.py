from data_structures_and_algorithms_401_python.Data_Structures.hashtable.hashtable import *
import pytest


def test_add_hashtable(prepared_hashtable):
    prepared_hashtable.add('Obada', 30)
    assert prepared_hashtable.get('Obada')==30

def test_get_hashtable(prepared_hashtable):
    actual=prepared_hashtable.get('ahmad')
    expected=25
    assert actual==expected

def test_get_hashtable_incorrect_key(prepared_hashtable):
    actual=prepared_hashtable.get('Mohammad')
    expected=None
    assert actual==expected


def test_collision_hashtable(prepared_hashtable):
    actual=prepared_hashtable.contains('hamad')
    expected=True
    assert actual==expected

def test_collision_value_hashtable(prepared_hashtable):
    actual=prepared_hashtable.get('hamad')
    expected=29
    assert actual==expected


def test_collision_value_hashtable(prepared_hashtable):
    actual=prepared_hashtable.hash('hamad')
    expected=417
    assert actual==expected





@pytest.fixture
def prepared_hashtable():
    hashtable = Hashtable(1024)
    hashtable.add('ahmad', 25)
    hashtable.add('hamad', 29)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    hashtable.add('class', 'Python-401d4')
    return hashtable