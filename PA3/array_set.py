""" This module contains an array based Set implementation

Author: Nathan Sprague
Version: 10/14/14
"""

# Some documentaion is borrowed from Python's built-in set type:
# Copyright 2001-2014 Python Software Foundation; All Rights Reserved

import t_array as t_array

# Turn off the array visualization.
t_array.Array.visible = False

class Set(object):
    """
    Array-based set class.  The functionality is almost exactly the same
    as Python's built-in set type.
    """

    def __init__(self, iterable=[]):
        """
        Set() -> new empty set object
        Set(iterable) -> new set object
        Build an unordered collection of unique elements.
        """
        self._array = t_array.Array(2)
        self._len = 0
        for item in iterable:
            self.add(item)

    def __eq__(self, rhs):
        """
        Two sets are equal if and only if every element of each set is
        contained in the other (each is a subset of the other).
        """
        return (type(self) == type(rhs) and
                self.issubset(rhs) and
                self.issuperset(rhs))

    def __ge__(self, rhs):
        """ Test whether every element in rhs is in the set. """
        return self.issuperset(rhs)

    def __gt__(self, rhs):
        """
        Test whether the set is a proper superset of rhs, that is,
        set >= rhs and set != rhs.
        """
        return self >= rhs and self != rhs

    def __le__(self, rhs):
        """ Test whether every element in the set is in rhs. """
        return self.issubset(rhs)

    def __lt__(self, rhs):
        """
        Test whether the set is a proper subset of rhs, that is,
        set <= rhs and set != rhs.
        """
        return self <= rhs and self != rhs

    def __ne__(self, rhs):
        """
        Two sets are equal if and only if every element of each set is
        contained in the other (each is a subset of the other).
        """
        return not self == rhs

    def __sub__(self, rhs):
        """
        Return a new set with elements in the set that are not in rhs.
        """
        return self.difference(rhs)

    def __len__(self):
        """ Return the number of elements in the set. """
        return self._len

    def __repr__(self):
        """ Return a string representation of the set. """
        result = "set(["
        for item in self:
            result += repr(item) + ", "
        result = result.rstrip(", ")
        return result + "])"

    def clear(self):
        """ Remove all elements from the set. """
        self._array.free()
        self._array = t_array.Array(2)
        self._len = 0

    def copy(self):
        """ Return a shallow copy of the set. """
        return Set(self)

    def add(self, item):
        """ Add element item to the set. """
        if item not in self:
            if self._len == len(self._array):
                self._resize()
            self._array[self._len] = item
            self._len += 1

    def difference(self, rhs):
        """
        Return a new set with elements in the set that are not in rhs.
        """
        if type(rhs) != Set:
            raise TypeError()
        new_set = Set()
        for item in self:
            if item not in rhs:
                new_set.add(item)
        return new_set

    def discard(self, item):
        """ Remove element item from the set if it is present. """
        indx = self._find(item)
        if indx != -1:
            self._remove_indx(indx)

    def remove(self, item):
        """
        Remove element item from the set. Raises KeyError if item is
        not contained in the set.
        """
        if item not in self:
            raise KeyError()
        else:
            self.discard(item)

    def _remove_indx(self, indx):
        """ Helper method for removing an element from a particular index.

        Removes and returns the item at the indicated index.
        (used in discard and pop.)
        """
        item = self._array[indx]
        for i in range(indx, len(self)):
            self._array[i] = self._array[i + 1]
        self._len -= 1
        return item

    def _find(self, item):
        """ Helper method for finding the index of a particular item

        Returns the index of the item or -1 if not found.
        """
        for i in range(len(self)):
            if self._array[i] == item:
                return i
        return -1

    def intersection(self, rhs):
        """ Return a new set with elements common to the set and rhs. """
        if type(rhs) != Set:
            raise TypeError()

        new_set = Set()
        for item in self:
            if item in rhs:
                new_set.add(item)
        return new_set

    def __and__(self, rhs):
        """ Return a new set with elements common to the set and rhs. """
        return self.intersection(rhs)

    def __del__(self):
        """ Free the the array because the garbage collector won't do it. """
        self._array.free()

    def union(self, rhs):
        """ Return a new set with elements from the set and rhs. """
        if type(rhs) != Set:
            raise TypeError()

        new_set = Set()
        for item in self:
            new_set.add(item)
        for item in rhs:
            new_set.add(item)

        return new_set

    def __or__(self, rhs):
        """ Return a new set with elements from the set and rhs. """
        return self.union(rhs)

    def symmetric_difference(self, rhs):
        """
        Return a new set with elements in either the set or rhs but not both.
        """
        return self.union(rhs) - self.intersection(rhs)

    def __xor__(self, rhs):
        """
        Return a new set with elements in either the set or rhs but not both.
        """
        return self.symmetric_difference(rhs)

    def pop(self):
        """
        Remove and return an arbitrary element from the set. Raises
        KeyError if the set is empty.
        """
        if len(self) == 0:
            raise KeyError()
        else:
            return self._remove_indx(len(self) - 1)

    def __iter__(self):
        """ Return an iterator for the set. """
        for i in range(len(self)):
            yield self._array[i]

    def _resize(self):
        """ Helper method for resizing the array when necessary """
        new_array = t_array.Array(len(self._array) * 2)
        for i in range(len(self._array)):
            new_array[i] = self._array[i]
        self._array.free()
        self._array = new_array

    def __contains__(self, item):
        """ Returns true if the item is contained in the set. """
        for element in self:
            if item == element:
                return True
        return False

    def isdisjoint(self, rhs):
        """
        Return True if the set has no elements in common with
        rhs. Sets are disjoint if and only if their intersection is
        the empty set.
        """
        if type(rhs) != Set:
            raise TypeError
        return len(self.intersection(rhs)) == 0

    def issubset(self, rhs):
        """ Test whether every element in the set is in rhs. """
        if type(rhs) != Set:
            raise TypeError
        return len(self.intersection(rhs)) == len(self)

    def issuperset(self, rhs):
        """ Test whether every element in rhs is in the set. """
        if type(rhs) != Set:
            raise TypeError
        return rhs.issubset(self)

def quick_tests():
    """ Just some simple tests created while writing methods. """
    a = Set()
    b = Set()
    a.add("tree")
    a.add("tree1")
    a.add("tree2")
    b.add("tree2")
    b.add("tree3")
    print(len(a))
    print("tree" in a)
    print(a)

    for item in a:
        print(item)

    print(a & b)
    print(a | b)
    print(a)
    a.discard("tree")
    a.discard("cow")
    print("dis", a)
    print(a.pop())
    print("popped", a)

    b.add('tree1')
    print()
    print("a", a)
    print("b", b)
    print(a.isdisjoint(b))
    print(a.issubset(b))
    print(b.issubset(a))
    print(a.issuperset(b))
    print(b.issuperset(a))
    print(a.issuperset(a))
    print(a - b)
    print(b - a)

    print(a < b)
    print(b < a)
    print(a > b)
    print(b > a)
    print(a <= b)
    print(a >= b)
    print(a == b)
    print(a == a)
    print(a <= a)
    print(a >= a)
    print(a < a)
    print(a > a)
    print(a & b & b)




if __name__ == "__main__":
    quick_tests()
