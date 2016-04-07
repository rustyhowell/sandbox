#!/usr/bin/env python

import unittest

example_list_with_integers = [[1, 2, 3, [[4]]], [[[[5]]]], 6]
example_list_with_strings = ['one', [['two']], [['three', 'four'], 'five'], [[['six']]]]

def flatten_deep_list(l):
    '''
    Flatten a list of arbitrarily nested lists of integers and strings
    :param l: The list to flatten
    :return: A flattened list
    '''
    new_list = []  # This recursive method creates and destroys a lot of lists. We can do better.
    for o in l:
        if isinstance(o, list):
            new_list.extend(flatten_deep_list(o))
        else:
            new_list.append(o)

    return new_list

def flatten_deep_list_2(l):
    '''
    Flatten a list of arbitrarily nested lists of integers and strings. This one only creates only one new list,
    no matter how deep the nested lists get.
    :param l: The list to flatten
    :return: A flattened list
    '''
    new_list = []
    def _flatten(_l, _new_list):  # This nested function appends to the new list without using temporary lists.
        for o in _l:
            if isinstance(o, list):
                _flatten(o, _new_list)
            else:
                _new_list.append(o)

    _flatten(l, new_list)
    return new_list

class Test_flatten_deep_list(unittest.TestCase):
    def test(self):
        l1 = example_list_with_integers
        e1 = [1, 2, 3, 4, 5, 6]

        l2 = example_list_with_strings
        e2 = ['one', 'two', 'three', 'four', 'five', 'six']

        l3 = example_list_with_strings + example_list_with_integers
        e3 = ['one', 'two', 'three', 'four', 'five', 'six', 1, 2, 3, 4, 5, 6]

        for l, expected in [(l1,e1),(l2,e2),(l3,e3)]:
            # Test both methods.
            new_l = list(flatten_deep_list(l))
            self.assertEqual(new_l, expected)

            new_l2 = list(flatten_deep_list_2(l))
            self.assertEqual(new_l2, expected)


if __name__ == '__main__':
        l1 = list(flatten_deep_list(example_list_with_integers))
        print(l1)

        l2 = list(flatten_deep_list(example_list_with_strings))
        print(l2)

        l3 = list(flatten_deep_list(example_list_with_strings + example_list_with_integers))
        print(l3)