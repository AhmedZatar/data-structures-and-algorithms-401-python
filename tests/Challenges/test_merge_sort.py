from data_structures_and_algorithms_401_python.Challenges.merge_sort.merge_sort import Mergesort



def test_random_sorted():
    arr=[8,4,23,42,16,15]
    Mergesort(arr)
    assert arr[0]==4
    assert arr[1]==8
    assert arr[-1]==42

def test_Reverse_sorted():
    arr=[20,18,12,8,5,-2]
    Mergesort(arr)
    assert arr[0]==-2
    assert arr[1]==5
    assert arr[-1]==20

def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    Mergesort(arr)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==12

def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    Mergesort(arr)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==12

def test_Nearly_sorted():
    arr=[2,3,5,7,13,11]
    Mergesort(arr)
    assert arr[0]==2
    assert arr[1]==3
    assert arr[-1]==13