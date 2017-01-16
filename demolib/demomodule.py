""" Python Demo module

Contains functions which are buggy or not generic
"""


def find_median(list_):
    """ returns the statistical median from list
    """
    # bugs: does not sort list
    # idx will be a float on Python 3
    # using sorted() function is a good idea as that doesn't modify the
    # original list
    idx = len(list_) // 2
    return sorted(list_)[idx]


def say_hello(hello):
    """ prints a statement """
    # breaks in python 3 as print is a function in python3
    print(hello)


class DemoClass(object):
    """ A simple class that has an unwieldy method
    """
    def do_silly_stuff(self):
        # this should take a while to compute on most modern computers
        #   also indentation is wonky
        self._value = sum(range(10000000000))

    def add(self, value):
        """ return stored value plus given value """
        self.do_silly_stuff()
        return self._value + value
