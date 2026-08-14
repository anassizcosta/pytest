from temperatura import celsius_para_fahrenheit

def test_1():
    assert celsius_para_fahrenheit(0) == 32

def test_2():
    assert celsius_para_fahrenheit(100) == 212

def test_3():
    assert celsius_para_fahrenheit(10) == 50
