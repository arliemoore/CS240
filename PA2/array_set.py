
'''
Created on Sep 29, 2014

This submission compiles with the JMU Honor Code. All code was written by
the submitter, and no unauthorized assistance was used while completing this
assignment.

@author: Arlie Moore
@date: 10/8/14
'''
from t_array import Array
from random import randint

class Set(object):
    '''Return a new Set object whose elements are taken 
    from optional parameter iterable. If iterable is not 
    specified, a new empty set is returned.'''
    
    
    def __init__(self, args = None):
        '''This constructor creates the Set() class. It 
        creates the underlying array and will iterate through
        any arguments sent into it and add it to the set.'''
        
        
        self._size = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)      #makes a fixed array with 1 capacity and size 0
        
        if args is not None:                    #If the object sent in is iterable
            for i in args:                      #then it adds each element to the set
                self.add(i)
                
    def __iter__(self):
        """Return an iterator for the set."""
        
        for i in range(len(self)-1, -1, -1):
            yield self._array[i]
                
    def __len__(self):
        '''Returns the length of the set'''
        
        return self._size
    
    def __eq__(self, other):
        """Returns true if the set is equal to another set. 
        Two sets are equal if and only if every element of each 
        set is contained in the other (each is a subset of the other). 
        If other is not a Set instance, this should return False."""
        
        result = False
        
        if isinstance(other, Set):          #Checks if other is a Set()
            if len(self) == len(other):
                if self <= other:
                    result = True
                
        return result
    
    def __ne__(self, other):
        '''self != other'''
        
        return not self.__eq__(other)       #Checks if self is equal to other, then switches it.
        
    def __str__(self):
        '''Calls the __repr__ method'''
        
        return self.__repr__()
    
    def __repr__(self):
        """Return a string representation of the set. 
        The format should be as follows: 'set([ELEMENT_1, ELEMENT_2,.
        .., ELEMENT_N])' Where the string representations of 
        each element should be obtained using the repr() method."""
        
        result = "set(["
        if len(self) == 0:
            result += "])"
        else:
            
            for i in range(len(self)):
                if isinstance(self._array[i], str):     #If _array[i] is a string then ' ' are needed around the element
                    if i == 0:                          #Special case for first element          
                        result += "'" + str(self._array[i]) + "'"
                    else:
                        result += str(", '" + str(self._array[i])) + "'"
                else:
                    if i == 0:                          #Special case for first element
                        result += str(self._array[i])
                    else:
                        result += str(", " + str(self._array[i]))
                
            result += "])"                          #Finishes off brackets
        
        return result
        
    def _make_array(self, c):
        '''Makes a new array of size "c" '''
        return Array(c)
    
    def _resize(self, newSize):
        '''Resizes self._array to the
        specified new size by creating a new
        array and copying all
        the items into it.'''
        
        B = self._make_array(newSize)       #Makes new array with a newSize
        for i in range(len(self)):          
            B[i] = self._array[i]           #Adds elements to the new resized array
            
        self._array = B                     #Assigns the new array to self
        self._capacity = newSize
            
    def add(self, elem):
        '''Add element elem to the set.'''
        
        if len(self) == self._capacity:        #Resizes array if needed
            self._resize(self._capacity * 2)
            
        if self.isIn(elem) == False:            #If the element is in the array already is does nothing
            self._array[self._size] = elem      #Else, adds the new element to self._array
            self._size = self._size + 1
    
    def remove(self, elem):
        '''Remove element elem from the set. Raises 
        KeyError if elem is not contained in the set.'''
        
        if self.isIn(elem) == True:         #If the element is in the array it removes
            self.discard(elem)
        else:                               #Else, it raises a KeyError
            raise KeyError("Element is not in the Set.")
    
    def discard(self, elem):
        '''Remove element elem from the set if it is present.'''
             
        if self.isIn(elem) == True:                         #If element is in the array it removes and shifts elements to the left
            new_array = self._make_array(self._capacity)    #Else, it does nothing
            for i in range(len(self)):
                new_array[i] = self._array[i]
                if self._array[i] == elem:
                    index = i
            size = self._size
            self.clear()
            for i in range(size):
                if i != index:
                    self.add(new_array[i])
        
    def pop(self):
        
        '''Remove and return an arbitrary element from the set. 
        Raises KeyError if the set is empty.'''
        
        if len(self) > 0:                       #If self has elements then it removes one randomly
            num = randint(0, self._size - 1)    #Random number between 0 and the size of the set
            result = self._array[num]
            self.remove(result)
        else:                                   #Else, raises a KeyError
            raise KeyError("The Set is empty.")
        
        return result
    
    def clear(self):
        '''Remove all elements from the set.'''
        
        B = self._make_array(self._capacity)
        self._array = B 
        self._size = 0
    
    def isIn(self, elem):
        '''Test x for membership in s.'''
        
        result = False
        
        for i in range(len(self)):
            if self._array[i] == elem:      #If the element is in the array then True is returned
                result = True
                break
        
        return result
    
    def isSet(self, other):
        '''Checks if "other" is a Set instance, 
        if it is then True is returned, if it is not
        then a TypeError is raised'''
        
        if isinstance(other, Set):          #If other is a Set() instance then True is returned
            return True
        else:
            raise TypeError("'Other' is not a Set() instance.")     #Else, TypeError is raised
        
    
    def isdisjoint(self, other):
        '''Return True if the set has no elements 
        in common with other. Sets are disjoint if 
        and only if their intersection is the empty set. 
        Raises a TypeError if other is not a Set instance.'''
        
        result = True
        
        self.isSet(other)
        
        for i in range(self._size):
            if other.isIn(self._array[i]):      #If an element is similar, false is returned
                result = False
                break  
        return result
                
    
    def issubset(self, other):
        '''Test whether every element in the set is in other. 
        Raises a TypeError if other is not a Set instance.'''
        
        return self.__le__(other)           #Calls __le__() (Less than or equal to)
    
    def issuperset(self, other):
        '''Test whether every element in other is in the set. 
        Raises a TypeError if other is not a Set instance.'''
        
        return self.__ge__(other)           #Calls __ge__() (Greater than or equal to)
    
    
    def __le__(self, other):
        '''self<=other'''
        
        result = True
        
        self.isSet(other)
        
        if len(self) <= len(other):                 
            for i in range(len(self)):
                if other.isIn(self._array[i]) == False:      #Checks if self._array[i] is in or not in other
                    result = False                           #If it is not in other, then False is returned
                    break
                    
        else:
            result = False                              #Returns False if len(self) <= len(other)
            
        return result
    
    def __ge__(self, other):
        '''self>=other'''
        
        result = True
        
        self.isSet(other)
        
        if len(self) >= len(other):             
            result = other.__le__(self)         #Checks if other is less than or equal too self
        else:
            result = False
            
        return result
    
    
    
    def __lt__(self, other):
        '''self<other'''
        
        result = False
        
        self.isSet(other)
        
        if self.__le__(other) and len(self) < len(other):   #Checks if self is less than or equal to other
            result = True
        
        return result
    
    def __gt__(self, other):
        '''self>other'''
        result = False
        
        self.isSet(other)
        
        if self.__ge__(other) and len(self) > len(other):       #Checks if self is greater than or equal to other
            result = True
            
        return result
    
    def union(self, other):
        '''Return a new set with elements from the set and 
        all others. Raises a TypeError if other is not a Set instance.'''
        
        
        result = Set()
        
        self.isSet(other)
            
        for i in range(len(self)):          
            result.add(self._array[i])
        for i in range(len(other)):
            result.add(other._array[i])
            
        return result
    
    def __and__(self, other):
        '''self & other'''
        
        return self.intersection(other)         #Calls intersection()
            
            
    def __or__(self, other):
        '''self | other'''
        
        return self.union(other)                #Calls union()
    
    def __xor__(self, other):
        '''self ^ other'''
        
        return self.symmetric_difference(other)     #Calls symmetric_difference()
        
    
    def intersection(self, other):
        '''Return a new set with elements common to the set 
        and all others. Raises a TypeError if other is not a Set instance.'''
        
        result = Set()
        
        self.isSet(other)
        
        for i in range(len(self)):
            if other.isIn(self._array[i]):  #Looks if self._arrya[i] is in the set Other
                result.add(self._array[i])  #Adds that element to the set result
                
        return result
            
    
    def difference(self, other):
        '''Return a new set with elements in 
        the set that are not in the others. 
        Raises a TypeError if other is not a Set instance.'''
        
        result = Set()
        
        self.isSet(other)
        
        for i in range(len(self)):
            if other.isIn(self._array[i]) == False:     #if self._array[i] is not in the set other
                result.add(self._array[i])              #then that element is added to the set result
                
        return result
    
    def symmetric_difference(self, other):
        '''Return a new set with elements in either 
        the set or other but not both. Raises a 
        TypeError if other is not a Set instance.'''
        
        result = Set()
        
        self.isSet(other)
        
        for i in range(len(self)):
            if other.isIn(self._array[i]) == False:     #if self._array[i] is not in the set other
                result.add(self._array[i])              #then that element is added to the set result
                
        for i in range(len(other)):
            if self.isIn(other._array[i]) == False:     #if other._array[i] is not in the set self
                result.add(other._array[i])             #then that element is added to the set result
                
        return result
        
        
    
    def copy(self):
        '''Return a new set with a shallow copy of s.'''
        
        
        new_set = Set()
        
        for i in range(len(self)):
            new_set.add(self._array[i])
            
        return new_set
    




