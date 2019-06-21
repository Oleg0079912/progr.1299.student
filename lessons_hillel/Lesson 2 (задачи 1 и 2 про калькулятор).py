########################Задания,
# Простой калькулятор 1, который делает различные подсчеты, но 0 < a < 9 and 0 < a < 9
def my_sum(a, b):
    return a + b

def my_dif(a, b):
    return a - b

def my_main(a, b):
    return a * b

def my_dil(a, b):
    return a / b

def calc(formula): # formula = a + b,  0 < a < 9 and 0 < a < 9
    a = int(formula[0])
    b = int(formula[2])
    s = formula[1]

    result = 0

    if s == "+":
        result = my_sum(a, b)
    elif s == "-":
        result = my_dif(a, b)
    elif s == "*":
        result = my_main(a, b)
    elif s == "/":
        result = my_dil(a, b)
    return result

res = calc("9+5")
print(res)

res = calc("9-5")
print(res)

res = calc("9*5")
print(res)

res = calc("9/5")
print(res)

###################################Задания,
# Простой калькулятор 2, который делает различные подсчеты, но уже с любыми числами
def my_sum(a, b):
    return a + b

def my_dif(a, b):
    return a - b

def my_main(a, b):
    return a * b

def my_dil(a, b):
    return a / b

def calc(formula):

    splitted = formula.split(" ")

    a = int(splitted[0])
    b = int(splitted[2])
    s = splitted[1]

    result = 0

    if s == "+":
        result = my_sum(a, b)
    elif s == "-":
        result = my_dif(a, b)
    elif s == "*":
        result = my_main(a, b)
    elif s == "/":
        result = my_dil(a, b)

    return result


res = calc("95252 + 45")
print(res)

res = calc("95252 - 45")
print(res)

res = calc("95252 * 45")

print(res)

res = calc("95252 / 45")
print(res)