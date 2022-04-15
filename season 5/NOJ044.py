class stack():
    def __init__(self):
        self.l = []
    def push(self, num):
        self.l.append(num)
    def pop(self):
        if len(self.l) >= 1:
            self.l.pop(-1)

stack1 = stack()
while True:
    command = input()
    if command[0] == '1':
        c, n = command.split(' ')
        stack1.push(int(n))
    elif command[0] == '2':
        stack1.pop()
    elif command[0] == '0':
        if len(stack1.l) == 0:
            print('')
        for i in range(len(stack1.l)):
            print(stack1.l[i], end=' ')
        break
