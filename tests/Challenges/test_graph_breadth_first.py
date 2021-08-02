import pytest
from data_structures_and_algorithms_401_python.Challenges.graph_breadth_first.graph_breadth_first import *






def test_happy_path():
    graph2 = Graph()
    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')
    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)

    actual=graph2.BreadthFirst(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,naboo,narina]
    assert actual==expected



def test_edge_case():
    graph2 = Graph()
    pandora=Vertix('pandora')
    
    actual=graph2.BreadthFirst(pandora)
    expected='This node is not in the graph'
    assert actual==expected


def test_expected_failure():
    graph2 = Graph()
    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')
    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)

    actual=graph2.BreadthFirst(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,narina,naboo]
    assert actual!=expected
