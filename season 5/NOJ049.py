class Bight:
    def __init__(self, num):
        self.num = num
        self.b = 1
        self.__b()
    def __b(self):
        for i in range(1, self.num+1):
            self.b *= i

num = int(input())
p = Bight(num)
print(int(p.b))
