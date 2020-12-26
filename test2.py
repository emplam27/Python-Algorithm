
def f():
    list_b = [[i for i in range(10)] for _ in range(10)]
    print(id(list_b[0][0]))


list_a = [[i for i in range(10)] for _ in range(10)]
print(id(list_a[0][0]))
f()