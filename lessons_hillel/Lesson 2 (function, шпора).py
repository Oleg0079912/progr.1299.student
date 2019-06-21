def first_method():
    print("Hello World")


def hello(name):
    print("Hello %s" % name)


def my_sum(a, b):
    return a + b

def Cacl(name, a, b):
    hello(name)
    return my_sum(a, b)

#вызываем функции и говорит что с ними делать, если нужно:
first_method()
hello("John")

res = Cacl("John", 10, 5)
res = my_sum(10, 5)
print(res)
