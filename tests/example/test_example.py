from .context import example

def test_func_pass1():
    assert example.func(3) == 4

def test_func_pass2():
    assert example.func(4) == 5
