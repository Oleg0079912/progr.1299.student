# Задача: нужно вести последовательность чисел: 2, 4, 7, 1... и
# и программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Решение без костыля

string = input()
counter = 1
i = 0

while (i + 1) < len(string):  # Проверяем, не последний ли символ, чтобы избежать out of range
    if string[i] == string[i + 1]:
        counter += 1
    else:
        print(string[i] + str(counter), end='')
        counter = 1

    i += 1
# Т.к. последняя последовательность отсекается, чтобы не случилось out of range, выводим остаток принудительно
print(string[i] + str(counter))

# Other methods
a = [int(i) for i in input().split()]
n = len(a)
#while (i + 1 ) < len(n):
for i in a:
    sum_1 = 0
    sum_1 = sum_1 + a[(i-1) % n] + a[(i+1) % n]
    print(sum_1, end=" ")



