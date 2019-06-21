# Задача - сделать таблицу умножения
# В строчку и таблицу.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for j in range(c, d+1):                 # stroka
    print('\t', j, end="")
for i in range(a, b+1):                 # stolbez
    print("\n", i, end="")
    for k in range(c, d+1):
        print('\t', i * k, end="")

