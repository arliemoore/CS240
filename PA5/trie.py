'''

@author: Arlie Moore
@date: 12/5/2014

Honor Code Statement:

#-------------------------------------------------------------------
# This submission compiles with the JMU Honor Code. All code was written by the
# submitter, and no unauthorized assistance was used while completing this
# assignment.
#
# - Arlie Moore
#-------------------------------------------------------------------

'''

class Trie():
    
    
    
    class _Node:
        """ Represents a node in a trie,
            with up to 26 neighbor references
        """

        def __init__(self, letter):
            """ Create new node """
            self.letter = letter
            self.below = dict()         #Contains references to all childern nodes
            self.black = False
            
            
    def __init__(self):
        '''Create a new empty Trie.'''
        self.root = Trie._Node(None)    #Creates root for the trie
        self.size = 0
    
    def __len__(self):
        '''Return the number of words stored in this Trie'''
        return self.size
    
    def __contains__(self, word):
        '''Return True if the word is in the Trie, False otherwise.'''
        
        cur = self.root
        word_length = len(word)
        count = 1
        
        for i in word:                      #For all letters in the word
            if i in cur.below:              
                cur = cur.below[i]
                if word_length == count and cur.black == False:     #If its the last letter and the node is white, return False
                    return False
            else:                       #If the letter is not in the childern, return False
                return False
            count += 1
            
        return True                     #returns True if the method runs completely through
    
    def __iter__(self):
        '''Return an iterator that will allow iteration over all words in
           the trie in lexicographical (alphabetical) order.'''
        
        cur = self.root
        
        for i in sorted(cur.below.keys()):                      #For all the childern in the root
            for k in self.iterator_helper(cur.below[i], ""):    #Starts recursion with all the childern
                yield k
        
        
    def iterator_helper(self, cur, word):
        '''Helper method for recursivly 
        going through the trie'''
        
        if cur.black == True:                           #If the node is black, yield the current word
            yield word + cur.letter
            
        for i in sorted(cur.below.keys()):              #Recursivly call all the childern of current.
            for k in self.iterator_helper(cur.below[i], word + cur.letter):
                yield k

                
   
    def insert(self, word):
        '''Insert the indicated word into the Trie. 
           This method has no effect if the word is already in the Trie.
           No Return value.'''
        
        cur = self.root
        
        word_length = len(word)
        count = 1
        
        for i in word:
            if i in cur.below:              #The child node exists already
                if word_length == count:    #If the last letter of the word is being added, make the node black and increment size 
                    cur = cur.below[i]
                    cur.black = True
                    self.size += 1
                else:                       #Else, go to the child node
                    cur = cur.below[i]
            else:                               #The child node does not exist
                if word_length == count:        #If the last letter of the word is being added, make the node black and increment size
                    new_node = Trie._Node(i)
                    new_node.black = True
                    self.size += 1
                    cur.below[i] = new_node
                else:                           #Else, make the new letter node and add it to the childern of current.
                    new_node = Trie._Node(i)
                    cur.below[i] = new_node
                    cur = cur.below[i]
            count += 1
        
    
    def contains_prefix(self, prefix):
        '''Return true if the indicated string is a word in the Trie or is a 
           prefix of any word in the Trie. Return False otherwise.'''
        
        cur = self.root                 
        for i in prefix:                
            if i in cur.below:      
                cur = cur.below[i]
            else:                   #If the letter is not one of the children nodes, return False
                return False
            
        return True
    
    def prefix_iter(self, prefix):
        '''Return an iterator that will allow iteration over all of the
           words in the trie that have the indicated prefix, in
           lexicographical (alphabetical) order.'''
        
        cur = self.root
        
        for i in prefix:                #This for loop moves current to the end
            if i in cur.below:          #of the prefix. Then sends it to the helper
                cur = cur.below[i]      #to finish finding the words with that prefix
            else:
                yield

        for k in self.iterator_helper(cur, prefix[0: len(prefix) - 1]):     #Uses the helper to find all the words below that prefix
            yield k
    

    
    
    
    
    
    
    
