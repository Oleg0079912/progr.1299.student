#Двмерный массив
'''
def show_matrix(matrix):
    for row in matrix: # запускает цикл каждый раз и у нас получается каждая  строка
        for x in row:  # выводит строку
            print(x, end=" ")
        print()

m = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


show_matrix(m)

# print(m)
# print(m[0])
# print(m[0][1])
'''

import random

def init_matrix(matrix, min_n, max_n):
    for i in range(len(matrix)):
        for j in range(len(len(matrix[0]))):
            matrix[i][j] = random.randint(min_n, max_n)


def show_matrix(matrix):
    for row in matrix:
        for x in row:
            print(x, end=" ")
        print()

n = 10
a = [[0]* n for i in range(n)]

init_matrix(a, 1, 101)

show_matrix(ф)










