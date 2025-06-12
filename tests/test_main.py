from tempconvert import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_c_to_f():
    assert celsius_to_fahrenheit(0) == 32.0
    assert round(celsius_to_fahrenheit(100), 2) == 212.0

def test_f_to_c():
    assert round(fahrenheit_to_celsius(32), 2) == 0.0
    assert round(fahrenheit_to_celsius(212), 2) == 100.0
