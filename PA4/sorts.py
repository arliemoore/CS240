""" This module contains several sorting algorithms.  Much of this code
is based on examples from:

(c) 2011 John Wiley & Sons, Data Structures and Algorithms Using
Python, by Rance D. Necaise.

Modifications by: Nathan Sprague and Mike Lam, October 2014.

Modified by: Arlie Moore

Honor Code Statement:

#-------------------------------------------------------------------
# This submission compiles with the JMU Honor Code. All code was written by the
# submitter, and no unauthorized assistance was used while completing this
# assignment.
#
# - Arlie Moore
#-------------------------------------------------------------------

"""

import math
import random


# Increase the default maximum call stack size so that quick sort
# will not crash when passed ordered lists.

import sys
sys.setrecursionlimit(50000)


# This global variable should be used to hold the threshold value
# for switching sorting algorithms. (100 is not a good default.)

MERGE_SORT_THRESHOLD = 13


class CountInt(int):
    """ A subclass of Python's built-in int class that counts the
    number of comparisons between objects of the class.

    A CountInt is exactly the same as an int, except the class-level
    variable num_comparisons is incremented during every comparison
    operation.
    """

    num_comparisons = 0
    
    def __cmp__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__cmp__(rhs)

    def __lt__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__lt__(rhs)

    def __gt__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__gt__(rhs)

    def __le__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__le__(rhs)

    def __ge__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__ge__(rhs)

    def __eq__(self, rhs):
        CountInt.num_comparisons += 1
        return super().__eq__(rhs)


class CountList(list):
    """ A subclass of Python's built-in list class that counts the
    number of assigment operations performed on instances of the
    class .

    A CountList is exactly the same as a list, except the class-level
    variable num_assignments is incremented during every assignment
    operation.
    """

    num_assignments = 0

    def __setitem__(self, indx, item):
        CountList.num_assignments += 1
        super(CountList, self).__setitem__(indx, item)


#####################
###  BASIC SORTS  ###
#####################

def selection_sort(items):
    """ Sort the values in items using the selection sort algorithm.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """

    for i in range(len(items) - 1):

        # Find the minimum value in the remainder of the list.
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        # Swap the minimum with the current item
        items[i], items[min_index] = items[min_index], items[i]

def insertion_sort(items):
    """ Sort the values in items using the insertion sort algorithm.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """

    for i in range(1, len(items)):
        cur = items[i]
        j = i
        while j > 0 and cur < items[j - 1]:
            items[j] = items[j - 1]
            j -= 1
        items[j] = cur

def binary_insertion_sort(items):
    """ Sort the values in items using the binary insertion sort
    algorithm.

    This implementation is inspired by the binary sort code in
    Arrays.java from OpenJDK 7.0.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """
    for i in range(1, len(items)):
        cur = items[i]

        # Use binary search to find the insertion point.
        start = 0
        end = i
        while start < end:
            mid = (start + end) // 2
            if cur < items[mid]:
                end = mid
            else:
                start = mid + 1

        final = start

        # Insert the current item.
        j = i
        while j > final:
            items[j] = items[j - 1]
            j -= 1
        items[final] = cur

def binary_insertion_sort_sublist(items, first, last):
    
    """ Sort the values in items from 
    first to last using the binary insertion sort
    algorithm.

    This implementation is inspired by the binary sort code in
    Arrays.java from OpenJDK 7.0.

    Arguments: items - a list of items that are mutually comparable.
               first - the first item to start sorting
               last - the last item to end the sort
    Returns:   None.  The list is sorted in place.
    """
    
    for i in range(first, last + 1):
        cur = items[i]

        # Use binary search to find the insertion point.
        start = first - 1
        end = i
        while start < end:
            mid = (start + end) // 2
            if cur < items[mid]:
                end = mid
            else:
                start = mid + 1

        final = start

        # Insert the current item.
        j = i
        while j > final:
            items[j] = items[j - 1]
            j -= 1
        items[final] = cur


#####################
###  MERGE SORTS  ###
#####################

def merge_sort(items):
    """ Recursively merge-sort the list items.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place (using temporary
               storage for merging).
    """
    _merge_sort(items, 0, len(items) - 1)

def _merge_sort(items, first, last):
    """ Recursively merge sort the portion of the list items from
    index first to last inclusive.
    
    
    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
    Returns:   None.  The list is sorted in place. (using temporary
               storage for merging).
    """

    if first < last:
        mid = (first + last) // 2
        _merge_sort(items, first, mid)
        _merge_sort(items, mid + 1, last)
        merge(items, first, mid, last)

def merge(items, first, mid, last):
    """ Merge two adjacent sorted sub-sequences contained in the list
    items.

    Arguments  items - A list of comparable keys.
               first - The starting index of the first sequence.
               mid   - The ending index of the first sequence.  (The
                       second sequence begins at mid+1.)
               last  - The ending index of the second sequence.

    Precondition:  The two sequences are sorted.
    """

    # Create a list to merge into:
    tmp = CountList([None] * (last - first + 1))

    a = first
    b = mid + 1
    i = 0

    # Perform comparisons until we reach the end of either sub-sequence.
    while a <= mid and b <= last:
        if items[a] < items[b]:
            tmp[i] = items[a]
            a += 1
        else:
            tmp[i] = items[b]
            b += 1
        i += 1

    # Copy remainder of the first sub-sequence (if necessary)
    while a <= mid:
        tmp[i] = items[a]
        a += 1
        i += 1

    # Copy remainder of the second sub-sequence (if necessary)
    while b <= last:
        tmp[i] = items[b]
        b += 1
        i += 1

    # Copy merged values back into the original list.
    for i in range(len(tmp)):
        items[first + i] = tmp[i]

def merge_sort_switch(items):
    
    """ Recursively merge-sort the list items.
        

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place (using temporary
               storage for merging).
    """
    
    _merge_sort_switch(items, 0, len(items) - 1)
   
   
def _merge_sort_switch(items, first, last):
    """ Recursively merge sort the portion of the list items from
    index first to last inclusive. Once the threshold is met, 
    the sort is sent over to binary insertion sort to finish 
    the smaller subset.
    
    
    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
    Returns:   None.  The list is sorted in place. (using temporary
               storage for merging).
    """
    
    if last - first < MERGE_SORT_THRESHOLD:
        binary_insertion_sort_sublist(items, first + 1, last)
    
    elif first < last:
        mid = (first + last) // 2
        _merge_sort_switch(items, first, mid)
        _merge_sort_switch(items, mid + 1, last)
        merge(items, first, mid, last)

#####################
###  QUICK SORTS  ###
#####################

def quick_sort(items):
    """ Sorts a list using the recursive quick sort algorithm.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """
    _quick_sort(items, 0, len(items) - 1)

def _quick_sort(items, first, last):
    """ Recursively quick sort the portion of the list items from
    index first to last inclusive.
    
    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
    Returns:   None.  The list is sorted in place.
    """
    if first < last:
        pos = partition(items, first, last, last)
        _quick_sort(items, first, pos - 1)
        _quick_sort(items, pos + 1, last)

def partition(items, first, last, pivot):
    """ Partitions the subsequence using the given index as the pivot.

    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
               last  - location of the pivot element.
    Returns:   None.  The list is partitioned in place.
    """

    pivot_value = items[pivot]

    # Swap the pivot into the last position temporarily
    items[pivot], items[last] = items[last], items[pivot]
    
    # Scan for values that are in the wrong partition
    # and swap them
    left = first
    right = last - 1    # Ignore pivot for now
    while left <= right:
        while left <= right and items[left] < pivot_value:
            left += 1
        while left <= right and pivot_value < items[right]:
            right -= 1
        if left <= right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1

    # Swap the pivot back into place
    items[left], items[last] = items[last], items[left]

    # Return the index position of the pivot value.
    return left

def quick_sort_median(items):
    """ Sorts a list using the recursive quick sort algorithm.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """
    
    _quick_sort_median(items, 0, len(items) - 1)

def _quick_sort_median(items, first, last):
    """ Recursively quick sort the portion of the list items from
    index first to last inclusive. The pivot point is found
    by finding the median value from the first, middle, and last
    slots in the list.
    
    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
    Returns:   None.  The list is sorted in place.
    """
    
    if first < last:
        mid = (first + last) // 2
        hold = [items[first], items[mid], items[last]]
        hold.sort()
        if (hold[1] == items[first]):
            pivot = first
        elif (hold[1] == items[mid]):
            pivot = mid
        else:
            pivot = last
        pos = partition(items, first, last, pivot)
        _quick_sort_median(items, first, pos - 1)
        _quick_sort_median(items, pos + 1, last)

def intro_sort(items):
    """ Sorts a list using the recursive quick sort algorithm.

    Arguments: items - a list of items that are mutually comparable.
    Returns:   None.  The list is sorted in place.
    """
    
    _intro_sort(items, 0, len(items) - 1, 0, 2 * math.log(len(items), 2), False)
    
def _intro_sort(items, first, last, depth, max_depth, done):
    """ Recursively quick sort the portion of the list items from
    index first to last inclusive. If the recurrsion depth exceeds
    2 * log 2 n then the sort is completed using merge_sort_switch.
    
    Arguments: items - a list of items that are mutually comparable.
               first - starting index of range to be sorted (inclusive).
               last  - ending index of range to be sorted (inclusive).
               depth - depth is incremented by one everytime this method runs
               max_depth - This is the max_depth that the recussion is aloud to go
               done - True if intro_sort is complete, false if not.
    Returns:   None.  The list is sorted in place.
    """
    
    depth += 1
    
    if depth > max_depth:
        _merge_sort_switch(items, first, last)
        done = True
        return
    elif done:
        return
    elif first < last:
        pos = partition(items, first, last, last)
        _intro_sort(items, first, pos - 1, depth, max_depth, done)
        _intro_sort(items, pos + 1, last, depth, max_depth, done)



