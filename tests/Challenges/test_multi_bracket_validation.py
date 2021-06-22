from data_structures_and_algorithms_401_python.Challenges.multi_bracket_validation.multi_bracket_validation import *

def test_happypath():
    assert multi_bracket_validation('{}') == True
    assert multi_bracket_validation('{}(){}') == True
    assert multi_bracket_validation('()[[Extra Characters]]') == True
    assert multi_bracket_validation('(){}[[]]') == True


def test_Expected_failure():
    assert multi_bracket_validation('{}{Code}[Fellows](())') != False
    assert multi_bracket_validation('[({}]') != True


def test_Edge_Case():
    assert multi_bracket_validation('(](') == False
    assert multi_bracket_validation('{(})') == False
    assert multi_bracket_validation('{') == False
    assert multi_bracket_validation(')') == False
    assert multi_bracket_validation('[}') == False

    




