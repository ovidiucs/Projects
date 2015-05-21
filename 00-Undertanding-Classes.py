__author__ = 'ovidiucs'
class MyClass:
    """A simple class"""
    i = 12345

    data = [2,3,4,5,6]
    def __init__(self):
        """Methods"""
        self.data = [1,2,3,4,5]

    def f(self):
        return "Hello World"

x = MyClass()
y = MyClass

print x.__doc__, x.data, x.f()
# instanta
print type(x)
# classobject
print type(y)

class initargu:
    def __init__(self, realpart, imagipart):
        self.r = realpart
        self.i = imagipart

a = initargu(3.0,-4.5)
# instance, float, float, 3.0, -4.5
print type(a), type(a.r), type(a.i), a.r, a.i

# class initargu has no attribute 'r'
# print initargu.r

# TypeError: __init__() takes exactly 3 arguments (1 given)
# print initargu().r
"""
The only operations understood by instance objects are attribute references.
There are two kinds of valid attribute names, data attributes and methods.
"""
