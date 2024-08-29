class Foo(object):
    def __mul__(self, other):
        print '__mul__'
        return other
    def __rmul__(self, other):
        print '__rmul__'
        return other

x = Foo()
2 * x # __rmul__
x * 2 # __mul__
