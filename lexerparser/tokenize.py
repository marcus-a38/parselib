import re

class Lexer():


    def __init__(self, custom_breaks=None):

        self.custom_breaks = custom_breaks


    def tokenize(self, str, tags_enabled=False):

        empty_entries = [' ', '']
        tokens = re.split('(\W)', str)
        tokens[:] = [token for token in tokens if token not in empty_entries]
    
        return [Token(token) for token in tokens]


    def defragment(self, token_list, bounds=(0,0)):

        if len(bounds) > 2: 
            raise ValueError('Range must only have a left and right bound.')
      
        left = bounds[0]
        right = bounds[1] - 1
        temp = ''

        try:
            for i in range(left, right):    
                temp += token_list[i].value+' '
            return temp

        except IndexError as e: 
            exit(f'Concatenation halted because {e}. Largest index is {i} and you inputted {right} as a right bound.')
      

class Token():

    index = 0
    tag_types = ['variable', 'keyword', 'delimiter', 'operator', 'value', 'comment']
  
    def __init__(self, curr):

        self.tag = None
        self.role = None
        self.expression_index = None
        self.line = None
        self.value = curr
        self.index = Token.index
