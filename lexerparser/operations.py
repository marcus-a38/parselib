# To be used in evaluating operations.
# Consider this a primitive interpreter-- or even a calculator!

class Wrapper(): # group 'Value' and 'Equation' as subclasses of 'Wrapper'
    pass


class Value(Wrapper):

    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value
    

class Equation(Wrapper):

    def __init__(self, a, b):
        self.left = a
        self.right = b


class Add(Equation):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(Equation):
    def eval(self):
        return self.left.eval() - self.right.eval()
    

class Mul(Equation):
    def eval(self):
        return self.left.eval() * self.right.eval()
    

class Div(Equation):
    def eval(self):
        return self.left.eval() // self.right.eval()
    

class TrueDiv(Equation):
    def eval(self):
        return self.left.eval() / self.right.eval()
    

class Mod(Equation):
    def eval(self):
        return self.left.eval() % self.right.eval()


class Exp(Equation):
    def eval(self):
        return self.left.eval() ** self.right.eval()

class Comparison(Equation):
    def eval(self):
        return self.left.eval() == self.right.eval()