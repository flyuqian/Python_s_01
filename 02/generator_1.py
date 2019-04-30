
# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a 
#         a, b = b, a + b

# # for x in fibon(1000):
# #     print(x)

# gen = fibon(100)
# print(next(gen))
# print(next(gen))
# print(next(gen))



items = [1, 2, 3, 4, 5]
squared = []
squared = list(map(lambda x: x**2, items))
print(squared);

itemsThan2 = list(filter(lambda x: x > 2, items))
print(itemsThan2)


from functools import reduce
adder = reduce(lambda x, y: x * y, items, 10)
print(adder)

state = "true_" if True else "false_"
print(state)