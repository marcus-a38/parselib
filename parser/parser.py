from ctypes import *
import heapq as heap # utilizing heaps for priority queue parsing
import init, grammar

tree_index_data = {} # structure index:expression/data

class Token():

    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value


class ParseTree():

    def __init__(self):

        self.root = 0
        self.curr = self.root
        self.next = None
        self.prev = None
        

    def get_root(self):
        pass


    def traverse(self):
        pass


class Node():

    def __init__(self):
        self.type = None
        self.start = None
        self.end = None
        self.line = None

    def insert_child(self):
        pass

    def get_type(self):
        pass

    def get_value(self):
        pass


class Parser():

    tree = ParseTree()

    def __init__(self, tokens):
        
        self.queue = [] # priority queue
        self.types = {}
        self.cache = {} # cache known evaluations
        self.tokens = tokens # storing tokens in a dict
        self.curr = Node()
        

    def parse(self):

        self.curr = Node()
        self.curr.priority = None
        self.push()

    
    def get_tokens(self):

        pass

    def get_parse_tree(self):

        pass


    def push(self): # experimenting with heaps to implement priority queue
        
        heap.heappush(self.queue, (self.curr.priority, self.curr))

    
    def interpret_heap(self):

        pass
        




