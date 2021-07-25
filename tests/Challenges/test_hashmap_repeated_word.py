from data_structures_and_algorithms_401_python.Challenges.hashmap_repeated_word.hashmap_repeated_word import *


def test_happy_path():
    book="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    
   
    actual=repeated_word(book)
    expected='summer' 
    assert actual==expected



def test_edge_case():
    actual=repeated_word()
    expected='the book is empty'
    
    assert actual==expected


def test_expected_failure():
    book = "Once upon a time, there was a brave princess who..."
    actual=repeated_word(book)
    expected='.' 
    assert actual!=expected