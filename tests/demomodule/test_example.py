import sys

from demolib.demomodule import find_median
from demolib.demomodule import say_hello
from demolib.demomodule import DemoClass

def test_find_median():
    """ tests the find_median function
    """
    assert find_median([1, 3, 2]) == 2
    list_ = [5, 4, 3] + [0] * 500
    assert find_median(list_) == 0
    assert find_median([1, 1, 0]) == 1

def test_say_hello(capsys):
    """ test the say_hello function
    """
    string = "example string"
    say_hello(string)
    out, err = capsys.readouterr()
    assert out.strip() == string

def test_democlass_add(mock):
    test_object = DemoClass()
    test_object.do_silly_stuff = mock.Mock()
    test_object._value = 1
    assert test_object.add(2) == 3
    assert test_object.do_silly_stuff.called
