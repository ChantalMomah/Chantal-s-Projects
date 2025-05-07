#instance variables
class Flower:
    kind = 'tulip'
    def __init__(self, name):
        self.name = name
a = Flower('lily')
b = Flower('rose')
print(a.kind)
print(b.kind)
print(a.name)
print(b.name)