from example import func

def test_func_pass():
    assert func(3) == 4

def test_func_fail():
    assert func(3) == 5
