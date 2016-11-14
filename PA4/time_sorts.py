""" Code for experimentally analyzing Python sorting Algorithms.

Author: Nathan Sprague and Mike Lam, October 2014

Modified By:

Honor Code Statement
"""

import time
import random
import sys
from sorts import *


def random_count_list(size):
    """ Return a randomly generated CountList of CountInts """
    items = CountList()
    for i in range(size):
        items.append(CountInt(random.randint(0, sys.maxsize)))
    return items

def ordered_count_list(size):
    """ Return an ordered CountList of CountInts """
    items = CountList()
    for i in range(size):
        items.append(CountInt(i))
    return items

def time_sorts(func, size_sorts, num_sorts, gen_function):
    """ Time several calls to the provided sorting function.

    This function repeatedly generates random CountLists of integers, and
    times the provided sorting function as it sorts those lists.  Average
    sorting times are returned.

    Arguments:  func         - a sorting function.
                size_sorts   - the size of the random lists to sort.
                num_sorts    - the number of trials to execute.
                gen_function - a function that returns a list of elements
                               to sort.  Should take a single argument
                               indicating the size of list to return.
    Returns:  A tuple containing three values.  All values are averaged
              accross num_sorts trials.
                  The average total sort time in seconds.
                  The average total number of comparisons.
                  The average total number of assignments.
    """
    total_time = 0.0
    total_comparisons = 0
    total_assignments = 0
    for i in range(num_sorts):
        items = gen_function(size_sorts)
        results = time_sort(func, items)
        total_time += results[0]
        total_comparisons += results[1]
        total_assignments += results[2]
    avg_time = total_time / num_sorts
    avg_comparisons = total_comparisons / num_sorts
    avg_assignments = total_assignments / num_sorts
    return (avg_time, avg_comparisons, avg_assignments)

def time_sort(func, items):
    """ Time a single call to the provided sorting function.

    Arguments:  func - a sorting function.
                items - a CountList to sort.
    Returns:  A tuple containing three values:
                  The total sort time in seconds.
                  The total number of comparisons.
                  The total number of assignments.
    """
    sorted_items = sorted(items)
    start = time.perf_counter()
    CountInt.num_comparisons = 0
    CountList.num_assignments = 0
    func(items)
    total_time = time.perf_counter() - start
    total_comparisons = CountInt.num_comparisons
    total_assignments = CountList.num_assignments
    if sorted_items != items:
        print("IMPROPERLY SORTED LIST!")
    return (total_time, total_comparisons, total_assignments)

def main():
    """ Execute timing code and print results. """

    num_sorts = 10

    fmt_str = "    {0:25s} {1:10.5f} {2:15.2f} {3:15.2f}"
    fast_sorts = [
        merge_sort, merge_sort_switch,                  # merge sorts
        quick_sort, quick_sort_median, intro_sort       # quick sorts
    ]
    all_sorts = fast_sorts + [
        selection_sort,                                 # selection sorts
        insertion_sort, binary_insertion_sort           # insertion sorts
    ]

    print("Sorting {} Random Lists of Size 100000".format(num_sorts))
    for sort in fast_sorts:
        results = time_sorts(sort, 100000, num_sorts, random_count_list)
        print(fmt_str.format(sort.__name__, results[0], results[1], results[2]))
    print()

    print("Sorting {} Random Lists of Size 5000".format(num_sorts))
    for sort in all_sorts:
        results = time_sorts(sort, 5000, num_sorts, random_count_list)
        print(fmt_str.format(sort.__name__, results[0], results[1], results[2]))
    print()

    print("Sorting {} Ordered Lists of Size 5000".format(num_sorts))
    for sort in all_sorts:
        results = time_sorts(sort, 5000, num_sorts, ordered_count_list)
        print(fmt_str.format(sort.__name__, results[0], results[1], results[2]))
    print()


if __name__ == "__main__":
    main()

