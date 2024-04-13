#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[2]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        for char, child in self.children.items():
            if child.isEndOfWord == True:
                suffixes.append(suffix + char)
            suffixes.extend(child.suffixes(suffix + char))

        return suffixes
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        
        for char in word:
            current.insert(char)
            current = current.children[char]
        # mark last node as leaf
        current.isEndOfWord = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[3]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        for char, child in self.children.items():
            if child.isEndOfWord == True:
                suffixes.append(suffix + char)
            suffixes.extend(child.suffixes(suffix + char))

        return suffixes


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[4]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# https://www.cs.usfca.edu/~galles/visualization/Trie.html

# In[5]:


# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');


# In[6]:
def test_suffixes(suffix, expected_result):
    node = MyTrie.find(suffix)
    result = node.suffixes() if node else None
    if result == expected_result:
        print("Pass")
    else:
        print("Fail")

# Test case: return all words when empty suffix
test_suffixes("", wordList)

# Test case: returns y when suffix trigonometr
test_suffixes("trigonometr", ["y"])

# Test case: returns ['hology', 'agonist', 'onym'] when suffix ant
test_suffixes("ant", ['hology', 'agonist', 'onym'])

# Test case: node not found when suffix doesn't match
test_suffixes("trololo", None)





