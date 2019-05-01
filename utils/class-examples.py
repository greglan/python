"""
Class examples
"""


class A:
    def __new__(clss, *args, **kwargs):
        """
        Called for the creation of the instance, so before __init__. Not a static method !
        :return:
        """
        instance = super(A, clss).__new__(clss)
        return instance

    def __init__(self, arg):
        """
        Called for initializing an instance
        """
        self.arg = arg

    def whoami(self):
        print("I am class A")


class B(object):
    def __new__(clss, *args, **kwargs):
        """
        Called for the creation of the instance, so before __init__. Not a static method !
        :return:
        """
        instance = super(B, clss).__new__(clss)
        return instance

    def __init__(self, b):

        self.b = b

    def whoami(self):
        print("I am class B")


class C(A):
    def __init__(self, a, b, c):
        super(C, self).__init__(0)  # Call super method
        # super().__init__(arg)  # Python 3 only
        self.c = c

    def whoami(self):
        print("I am class C")


class D(A, B):
    def __init__(self):
        super().__init__(None)  # __init__ of A called


issubclass(A, object)  # Always return True
type("string")  # Return the type of an object
isinstance("string", str)  # Check type of an object
# ?A  # Information on the class

D().whoami()  # Method of class A because first class specified
