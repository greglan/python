"""
Main methods to override:
 - __str__
 - __ne__, __le__, __lt__, __ge__, __gt__
 - __add__, __sub__, __mul__, __div__, __floordiv__ (//), __rmul__ (right multiplication)
"""

class A:
    def __new__(self):  # Called for the creation of the instance
        self.x = None
        self.y = None

    def __init__(self, a, b):  # Called for initializing an instance
        self.x = a
        self.y = b

class B(A):
    def __init__(self, a, b, c):
        super(B, self).__init__(a, b)  # Call super method
        # super().__init__(a, b)  # Python 3 only
        self.c = c


?B  # Information on the class
issubclass(A, object)  # Always return True
type("string")  # Return the type of an object
isinstance(var, type)  # Check type of an object
