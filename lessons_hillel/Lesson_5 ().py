# Повторение материала
# игра 2048

def move_right(line): # числа справа, нули слево
    i = 0
    while i < len(line):
        j = 0
        while j < len(line) - 1:
            if line[j + 1] == 0 and line[j] != 0:
                c = line[j]
                line[j] = line[j + 1]
                line[j + 1] = c
            j += 1

        i += 1
    print(line)

def move_left(line): # числа слево, нули справа
    i = 0
    while i < len(line):
        j = 0
        while j < len(line) - 1:
            if line[j] == 0 and line[j + 1] != 0:
                c = line[j]
                line[j] = line[j + 1]
                line[j + 1] = c
            j += 1

        i += 1
    print(line)

def mov_matrix(matrix): # ф. идет по всей матрице и выполняет ф. def move_left(line)
    for row in matrix:
        move_left(row)


def coulm(matrix):
    x = 0
    while x < len(line): # ДОРАБОТАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        i = 0
        for i in range(len(matrix)):

            for j in range(len(matrix) - 1):
                if matrix[j][i] == 0 and matrix[j + 1][i] != 0:
                    c = matrix[j][i]
                    matrix[j][i] = matrix[j + 1][i]
                    matrix[j + 1][i] = c
                j += 1

            i += 1
        print(matrix)

line = [[0, 0, 1, 1], [0, 1, 2, 2], [2, 0, 4, 4], [4, 0, 0, 2]]

#move_right(line)
#move_left(line)
print(line)
#mov_matrix(line)
coulm(line)