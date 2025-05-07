#init method
class Add:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
        self.sum = num1 + num2
x = Add(17, 18)
print(x.a)
print(x.b)
print(x.sum) 