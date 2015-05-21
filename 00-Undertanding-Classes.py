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
http://www.pythontutor.com/visualize.html#code=class+MyClass%3A%0A++++%22%22%22A+simple+class%22%22%22%0A++++i+%3D+12345%0A%0A++++data+%3D+%5B2,3,4,5,6%5D%0A++++def+__init__(self)%3A%0A++++++++%22%22%22Methods%22%22%22%0A++++++++self.data+%3D+%5B1,2,3,4,5%5D%0A%0A++++def+f(self)%3A%0A++++++++return+%22Hello+World%22%0A%0Ax+%3D+MyClass()%0Ay+%3D+MyClass%0Aprint+x.f()%0A%0Aclass+initargu%3A%0A++++def+__init__(self,+realpart,+imagipart)%3A%0A++++++++self.r+%3D+realpart%0A++++++++self.i+%3D+imagipart%0A++++++++%0Aa+%3D+initargu(3.0,-4.5)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0
"""
