class Person(object):
    def __init__(self, count):
        self.count = count+1

count = 0
a = Person(count)
b = Person(a.count)
c = Person(b.count)
d = Person(c.count)
e = Person(d.count)
print(e.count)
