__author__ = 'horton'

import unittest
from graph import Graph

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.gr1 = Graph(
            { 'a': ['b', 'c', 'd'], 'b': ['a', 'd'], 'c' : ['a'], 'd' : ['b', 'a'], 'e' : []}
        )
        self.copy_gr1 = Graph(
            { 'a': ['b', 'c', 'd'], 'b': ['a', 'd'], 'c' : ['a'], 'd' : ['b', 'a'], 'e' : []}
        )


    def test_get_adjlist1(self):
        """G7: get_adjlist('a') should return ['b', 'c', 'd']"""
        # assume this is test-case with ID of G7 -- put that in the docstring and msg below
        a_val = self.gr1.get_adjlist('a')
        self.assertEqual(a_val, ['b', 'c', 'd'], msg="G7: get_adjlist('a') should return ['b', 'c', 'd']")

    def test_get_adjlist2(self):
        val = self.gr1.get_adjlist('e')
        self.assertEqual(len(val), 0, msg="get_adjlist('e') should return []")

    def test_get_adjlist3(self):
        self.assertIsNone(self.gr1.get_adjlist('z'), msg="get_adjlist(n) should return None if n not in graph")


    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()




# def test_is_complete1():
#     """ testing is_complete() with empty graph"""
#     empty = Graph( {} )
#     assert is_complete(empty) == True, "is_complete() with empty graph should return True"

# def test_is_complete2():
#     """ testing is_complete() with graph with one node"""
#     gr1 = Graph( {'a' : []} )
#     assert is_complete(gr1) == True, "is_complete() with one node should return True"

