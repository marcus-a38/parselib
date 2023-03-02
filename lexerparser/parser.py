import variables, operations, tokenize

class Tag(): # Again, grouping 'token type' classes together under parent 'Tag'
    pass

class Key(Tag):
# To hold raw strings of each python keyword, AND user-defined keys in microlanguages

    def __init__(self, keys: list):
        self.keys = keys


class Delimiter(Tag):

    def __init__(self, char: str):

        self.char = char.value
        self.index = char.index

        if self.char in ['(', '[', '{']:
            self.is_open = True
        else:
            self.is_open = False


class Parser():

    def __init__(self):
        self.tokens = None
        self.types = tokenize.Token.tag_list 
        self.lines = []
        self.queue = []
        

    def __make_expression__(self):
        # call 'defragment()' from tokenize.Token to join a complete expression back together.
        # for example, if token_list contains ['(', '3', '+', '5', ')'] at indeces 0-4,
        # this method will return a string expression '(3 + 5)'  
        pass
        

    def __group__(self, tokens): 

        line = ''
    
        for token in tokens:
            if token.type in 'open_d':
                pass



    def parse(self, tokens: list) -> list:

        self.tokens = tokens
        for token in tokens:
            for type in self.types:
                pass

        

        
        


