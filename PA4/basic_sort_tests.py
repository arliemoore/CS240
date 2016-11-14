"""
Basic unit tests for CS 240 PA 4 (Sorting Improvements).

Professor Lam
Nov 2014
"""

import unittest
import random
import os

import sorts as student

class BasicSortTests(unittest.TestCase):
    """ Basic sorting tests. """

    def _test_sort(self, sort, include_indices=False):
        items = [i for i in range(20)]
        random.shuffle(items)
        correct = sorted(items)
        if include_indices:
            sort(items, 0, len(items)-1)
        else:
            sort(items)
        self.assertEqual(items, correct)

    def test_selection_sort(self):
        self._test_sort(student.selection_sort)

    def test_insertion_sort(self):
        self._test_sort(student.insertion_sort)

    def test_binary_insertion_sort_sublist(self):
        self._test_sort(student.binary_insertion_sort_sublist, True)

    def test_merge_sort(self):
        self._test_sort(student.merge_sort)

    def test_merge_sort_switch(self):
        self._test_sort(student.merge_sort_switch)

    def test_quick_sort(self):
        self._test_sort(student.quick_sort)

    def test_quick_sort_median(self):
        self._test_sort(student.quick_sort_median)

    def test_intro_sort(self):
        self._test_sort(student.intro_sort)
'''
    def test_eval_present(self):
        self.assertTrue(os.path.isfile("eval.txt"))
'''        
if __name__ == "__main__":
    unittest.main()

