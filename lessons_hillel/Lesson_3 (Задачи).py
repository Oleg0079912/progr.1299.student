import random

def init_matrix(matrix, min_n, max_n):                  # заполняем случаными числами матрицу
    for i in range(len(matrix)):                        # проходим по след строке (запоняем)
        for j in range(len(matrix[0])):                 # проходим по строке (запоняем)
            matrix[i][j] = random.randint(min_n, max_n)


def show_matrix(matrix):                                # выводим каждую строку матрицы
    for row in matrix:
        for x in row:
            print(x, end=" ")
        print()


def min_max(matrix):                # Находим максимальное и минимальное значение каждой строки:
    i = 0
    for row in matrix:
        my_min = matrix[i][0]
        my_max = matrix[i][0]

        for l in row:
            if my_min > l:
                my_min = l

            if my_max < l:
                my_max = l
        i = i + 1

        print("Your number max:", my_max)
        print("Your number min:", my_min)
        print()


def min_max_in_all_matrix(matrix):      # Находим максимальное и минимальное значение всей матрицы:
    my_min = matrix[0][0]
    my_max = matrix[0][0]

    for row in matrix:
        for l in row:
            if my_min > l:
                my_min = l

            if my_max < l:
                my_max = l

    print("Your number max in all matrix:", my_max)
    print("Your number mix in all matrix:", my_min)
    print()


n = 10
matrix = [[0] * n for i in range(n)]                         # заполняем матрицу нулями

init_matrix(matrix, 1, 101)

show_matrix(matrix)
min_max(matrix)
min_max_in_all_matrix(matrix)



#  ДЗ: найти сумму четных и нечетных числен для всей матрицы
