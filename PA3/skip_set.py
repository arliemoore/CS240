"""
CS 240 Fall 2014
PA3: Skip List

Author: Arlie Moore
Date: 10/24/14
"""

#-------------------------------------------------------------------
# This submission compiles with the JMU Honor Code. All code was written by the
# submitter, and no unauthorized assistance was used while completing this
# assignment.
#
#
# - Arlie Moore
#-------------------------------------------------------------------

import random

class SortedSet:
    """ SortedSet ADT implemented using a skip list.
        Maintains elements in standard sorted order.
        Single-level nodes with next and below pointers.
        Uses sentinel values at the beginning of the skip list.
        Uses "coin tosses" to determine insertion heights.
    """

    class _Node:
        """ Represents a single-level node in a skip list,
            with two-way neighbor references
        """

        __slots__ = 'value', 'next', 'below'    # performance optimization

        def __init__(self, value):
            """ Create new node """
            self.value = value
            self.next = None
            self.below = None

        def __str__(self):
            return str(self.value)


    def __init__(self, iterable=[]):
        """ Create a new (empty) skip list """
        self._height = 0
        self._head = SortedSet._Node(None)
        self._len = 0
        for elem in iterable:
            self.add(elem)

    def viz(self):
        """ Returns a formatted textual representation of the list """
        width = 5           # column width
        reps = []           # string representations of rows
        curs = []           # list of pointers for simultaneous traversal

        # start by adding all sentinels to "curs"
        cur = self._head
        while cur is not None:
            curs.append(cur)
            reps.append("")
            cur = cur.below

        # follow one "next" reference at a time on the lowest layer
        lowest = curs[-1]
        while lowest is not None:
            for i in range(len(curs)):
                # advance each reference if we've reached a node that matches
                # the node on the bottom of the list
                if curs[i] is not None and curs[i].value == lowest.value:
                    reps[i] += str(curs[i]).center(width)
                    curs[i] = curs[i].next
                else:
                    reps[i] += "".center(width)
            lowest = lowest.next
        return "\n".join(reps) + "\n------------------"

    def add(self, value):
        """ Insert a value into the skip list; doesn't allow duplicates """      
        
        if value in self:
            return
        
        h = 0
        self._len += 1
        
        while (random.randrange(2) == 0):   #Counts how many times "heads" is flipped
            h += 1
            
        while h >= self._height:                #Adds new rows if h is greater than or equal to the height
            self.addRow()

        cur = self._head
        heightHolder = self._height
        
        while cur.below is not None:        #While cur has not run off the bottom of the list
            heightHolder -= 1               
            cur = cur.below                 #Current is dropped down to the next level
            if heightHolder <= (h):         #If insertion should happen at this height, then insertion will happen
                if heightHolder == (h):     #If this is first insertion, a node is created
                    new_node = SortedSet._Node(value)   
                if cur.next is None:        #If this is the first insertion in this row, then next will be none
                    cur.next = new_node
                    new_node = SortedSet._Node(value)
                    cur.next.below = new_node
                else:                       #Else, find the insertion point on this row
                    done = False
                    while cur.next is not None and not done:    #While cur has not run off the end of the row
                        if cur.next.value > value:
                            new_node.next = cur.next
                            cur.next = new_node
                            new_node = SortedSet._Node(value)
                            cur.next.below = new_node
                            done = True
                        if not done:                    #If not done, cur goes to next
                            cur = cur.next
                    if not done:                        #If not done, insert at the end of the row
                        cur.next = new_node
                        new_node = SortedSet._Node(value)
                        cur.next.below = new_node
            if heightHolder == 0:                       #If heightHolder is at the bottom, end.
                return

    def addRow(self):
        '''Helper Method - Adds a new row to the SortedSet'''
        new_head = SortedSet._Node(None)
        new_head.next = None
        new_head.below = self._head
        self._head = new_head
        self._height += 1               #Adds 1 to height
        
        
        
    def remove(self, value):
        """ Find and remove a value from the skip list.
            Raises a KeyError if the value is not in the list.
        """
        
       
        found = False
        cur = self._head
        
        while cur is not None:          
             
            while cur.next is not None:
                if cur.next.value == value:
                    cur.next = cur.next.next    #removes the value from the skip list
                    found = True                #The value is in the skip list
                elif cur.next.value < value or cur.below is None:
                    cur = cur.next
                else:
                    cur = cur.below
                    
            cur = cur.below             #moves down to the next row
            
            
        if not found:
            raise KeyError(value, "not in the Set.")
            
        self._len -= 1

    def __contains__(self, value):
        """ Returns True if the given value is in the list; False otherwise """
        
        if self._len == 0:
            return False
    
        cur = self._head
        
        while cur is not None:
             
            while cur.next is not None:
                if cur.next.value == value:
                    return True                 #returns True if its found
                elif cur.next.value < value or cur.below is None:
                    cur = cur.next
                else:
                    cur = cur.below
                    
            cur = cur.below
            
        return False


    def __iter__(self):
        """ Returns an iterator for the list """
        
        cur = self._head
        
        while cur.below is not None:        #Gets cur to the very bottom of the skip list
            cur = cur.below
            
        cur = cur.next
        while cur is not None:              #Goes through height zero and yields all values
            yield cur.value
            cur = cur.next



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
        self._head = SortedSet._Node(None)
        self._len = 0
        self._height = 0

    def copy(self):
        """ Return a shallow copy of the set. """
        return SortedSet(self)

    def difference(self, rhs):
        """
        Return a new set with elements in the set that are not in rhs.
        """
        if type(rhs) != SortedSet:
            raise TypeError()
        new_set = SortedSet()
        for item in self:
            if item not in rhs:
                new_set.add(item)
        return new_set

    def discard(self, item):
        """ Remove element item from the set if it is present. """
        
        try:
            self.remove(item)
        except KeyError:
            pass


    def intersection(self, rhs):
        """ Return a new set with elements common to the set and rhs. """
        if type(rhs) != SortedSet:
            raise TypeError()

        new_set = SortedSet()
        for item in self:
            if item in rhs:
                new_set.add(item)
        return new_set

    def __and__(self, rhs):
        """ Return a new set with elements common to the set and rhs. """
        return self.intersection(rhs)

    def union(self, rhs):
        """ Return a new set with elements from the set and rhs. """
        if type(rhs) != SortedSet:
            raise TypeError()

        new_set = SortedSet()
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
        
        for i in self:
            self.remove(i)
            return i
            
            


    def isdisjoint(self, rhs):
        """
        Return True if the set has no elements in common with
        rhs. Sets are disjoint if and only if their intersection is
        the empty set.
        """
        if type(rhs) != SortedSet:
            raise TypeError
        return len(self.intersection(rhs)) == 0

    def issubset(self, rhs):
        """ Test whether every element in the set is in rhs. """
        if type(rhs) != SortedSet:
            raise TypeError
        return len(self.intersection(rhs)) == len(self)

    def issuperset(self, rhs):
        """ Test whether every element in rhs is in the set. """
        if type(rhs) != SortedSet:
            raise TypeError
        return rhs.issubset(self)


def main():

    pass
    

if __name__ == "__main__":
    main()   
    
    

