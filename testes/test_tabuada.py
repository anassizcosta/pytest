from tabuada import tabuada

def test_1():
    assert tabuada(5) == [5,10,15,20,25,30,35,40,45,50]

def test_2():
    assert tabuada(2)[0] == 2

def test_3():
    assert tabuada(10)[-1] == 100
