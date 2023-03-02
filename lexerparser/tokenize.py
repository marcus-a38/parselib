import re

class Lexer():


    def __init__(self, custom_breaks: list=None):

        self.custom_breaks = custom_breaks 
        # To add: custom breaks, or user-defined separators to be used in tokenization

    def tokenize(self, input: str, tags_enabled: bool=False) -> list:

        empty_entries = [' ', '']
        tokens = re.split('([^a-zA-Z0-9+\.])', str) # changed from \W to something more comprehensive to keep floats intact
        tokens[:] = [token for token in tokens if token not in empty_entries]
    
        return [Token(token) for token in tokens]


    def defragment(self, tokens: list, bounds: tuple=(0,0)):
        # Join a range of tokens from a token list back together

        if len(bounds) > 2: 
            raise ValueError('Range must only have a left and right bound.')
      
        left = bounds[0]
        right = bounds[1] - 1
        temp = ''

        try:
            for i in range(left, right):    
                temp += tokens[i].value+' '
            return temp

        except IndexError as e: 
            exit(f'Concatenation halted because {e}. Largest index is {i} and you inputted {right} as a right bound.')
      

class Token(): 
# Initialize an object of class Token by pushing a string in. 
# Token 'metadata' will not be defined yet, the parser will do that.

    index = 0
  
    def __init__(self, curr):

        self.tag = 'None'
        self.role = 'None'
        self.expression_index = 'None'
        self.line = 'None'
        self.value = curr
        self.index = Token.index
