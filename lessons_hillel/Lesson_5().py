# Повторение материала
# игра 2048
# Запустить и все пойму какое задание по этому коду
def move_right(line):
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

def move_left(line):
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


line = [0, 0, 1, 0, 1, 2, 2, 0, 4, 4, 0]

move_right(line)
move_left(line)
