from data_structures_and_algorithms_401_python.Challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest


def test_happypath_return_cat_name(queue_vals):
    actual = queue_vals.dequeue('cat')
    expected = 'snow'
    assert actual == expected

def test_Expected_failure_return_wrong_dog_name(queue_vals):
    actual = queue_vals.dequeue('dog')
    expected = 'mert'
    assert actual != expected

def test_Edge_Case_return_None(queue_vals):
    actual = queue_vals.dequeue('hores')
    expected = None
    assert actual == expected


@pytest.fixture
def queue_vals():
    dj = Dog('dj')
    boby=Dog('boby')
    mert=Dog('mert')
    snow = Cat('snow')
    amy=Cat('amy')
    mshmsh=Cat('mshmsh')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(dj)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mert)
    animalShelter.enqueue(snow)
    animalShelter.enqueue(amy)
    animalShelter.enqueue(mshmsh)
    return animalShelter
