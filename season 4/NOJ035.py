def work():
    x = 0

    def new_work():
        nonlocal x
        x += 1
        return x
    return new_work


a = work()
for i in range(5):
    print(a())

# def outer(x):
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner
#
# a = outer(0)
# for i in range(5):
#    print(a())