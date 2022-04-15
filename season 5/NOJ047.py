class Calculate:
    def cal(self, num1, oper, num2):
        exec('self.a = ' + num1 + oper + num2)
        return self.a

num1, oper, num2 = input().split(' ')
C = Calculate()
print(int(C.cal(num1, oper, num2)))
