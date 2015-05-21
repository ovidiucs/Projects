__author__ = 'ovidiucs'

class Reverse:
    def __init__(self,string):
        self.string=string[::-1]

# at class instantiation
x = Reverse("LeGrand")

print x.string