import pytest
from data_structures_and_algorithms_401_python.Challenges.graph_business_trip.graph_business_trip import *




def test_happy_path():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)

    actual=business_trip(graph2,[metroville,pandora])
    expected=(True, '$82')
    assert actual==expected



def test_edge_case():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)
    
    actual=business_trip(graph2,[arendelle,manstropolis, naboo])
    expected=(False, '$0')
    assert actual==expected


def test_expected_failure():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)

    actual=business_trip(graph2,[arendelle,manstropolis, naboo])
    expected=(True, '$82')
    assert actual!=expected
