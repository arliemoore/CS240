"""
CS 240 Fall 2014
PA3: Linked List

Author: Arlie Moore
Date: 10/24/14
"""
from email._header_value_parser import get_value

#-------------------------------------------------------------------
# This submission compiles with the JMU Honor Code. All code was written by the
# submitter, and no unauthorized assistance was used while completing this
# assignment.
#
# - Arlie Moore
#-------------------------------------------------------------------

class LinkedList:
    """ Python implementation of a singly-linked list.
        Maintains elements in standard sorted order.
        Uses sentinel value at the beginning of the list.
    """

    class _Node:
        """ Represents a node in a singly-linked list """

        __slots__ = 'value', 'next'     # performance optimization

        def __init__(self, value, next=None):
            """ Create new node """
            self.value = value
            self.next = next


    def __init__(self):
        """ Create a new (empty) linked list """
        self._head = LinkedList._Node(None)

    def viz(self):
        """ Returns a formatted textual representation of the list """
        text = []
        cur = self._head
        while cur is not None:
            text.append(str(cur.value))
            cur = cur.next
        return " -> ".join(text)

    def add(self, value):
        """ Insert a value into the linked list; doesn't allow duplicates """
        
        new_node = LinkedList._Node(value)
        cur = self._head.next
        previous = self._head
        
        while cur is not None:
            if cur.value == value:
                return
            if cur.value > value:
                previous.next = new_node
                new_node.next = cur
                return
            previous = cur
            cur = cur.next
            
        previous.next = new_node
        new_node.next = None

    def remove(self, value):
        """ Find and remove a value from the linked list.
            If there are multiple instances it will only remove one.
            Raises a KeyError if the value is not in the list.
        """
        cur = self._head.next
        previous = self._head

        while cur is not None:
            if cur.value == value:
                previous.next = cur.next
                return
            previous = cur
            cur = cur.next
            
        raise KeyError(value, "not in list.")
            
        

    def __contains__(self, value):
        """ Returns True if the given value is in the list; False otherwise """
        
        for i in self:
            if i == value:
                return True
            
        return False

    def __iter__(self):
        """ Returns an iterator for the list """
        cur = self._head.next
        
        while cur is not None:
            yield cur.value
            cur = cur.next
    
    
    
    
def main():
    
    # ADD NEW TESTS!
    test = LinkedList()
    test.add("z")
    test.add("y")
    test.add("a")
    test.add("b")
    test.add("d")
    test.add("c")
    test.add("cat")
    test.add("dogs")
    test.add("m")
    
    for i in test:
        print(i)
    
    print("cat" in test)
    print(test.viz())
    
if __name__ == "__main__":
    main()   
    
    



