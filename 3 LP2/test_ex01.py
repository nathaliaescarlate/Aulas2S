# content of test_sample.py
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def test_answer():
    assert inc(3) == 4 or dec(3) == 99

def test_answer2():
    assert inc(20)==21

def test_answer3():
    assert inc(98)==99