import re

def verify_token(method):

    def inner(token):
        if token in '' or token in ' ':
            raise TypeError('Token cannot be empty.')
        else:
            return method(token)
    return inner()


class Token():

    index = 0
    tags = ['variable', 'keyword', 'delimiter', 'operator', 'value', 'comment']

    @verify_token
    def __init__(self, token, tag='None', role='None'):

        if tag not in 'None': self.tag = tag
        if role not in 'None': self.role = role
        self.value = token
        self.index = Token.index
        Token.index += 1


    def create_tags():
        pass


    def tokenize(str, tags_enabled=False):

        empty_entries = [' ', '']

        tokens = re.split('(\W)', tokens)
        tokens[:] = [token for token in tokens if token not in empty_entries]

        if tags_enabled:
            pass
        else:
            pass

        return tokens


class Queue():

    def __init__(self, tokens):
        self.queue = tokens


    def push_queue(self, target):
        for i in len(self.queue):
            target(self.queue.pop(i))

# UNFINISHED!

                
            









