from .context import example

def test_func_pass():
    assert example.func(3) == 4

def test_func_fail():
    assert example.func(3) == 5
