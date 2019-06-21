import random
class Field:

    def __init__(self, x, y): # функция (конструктор) заполняет ячейки нулями
        self.x = x
        self.y = y
        self.my_field = [[0 for x in range(x)] for y in range(y)]  #заполняем нулями строки "x"

    def init_bombs(self): # кол-во бомб и разместит их.
        number_of_bombs = (self.x * self.y) * 25 / 100 # 25%. Исп чтобы бомб было 25% от всего кол-ва

        n = 0

        while n < number_of_bombs:                # Делаем n , чтобы мы шли до 25%, как по примеру
            b_x = random.randint(0, self.x - 1)   # оно генеирует случайное число "х" . Пусть = 2
            b_y = random.randint(0, self.y - 1)   # оно генеирует случайное число "у" . Пусть = 3
                                                  # и вот по этим координатам (2, 3) мы идем в if
    # насчет нюанса (0, self.x - 1), Мы делаем промежуток от 0 до 9(10-1, как по примеру (10, 10).
            if self.my_field[b_x][b_y] == 0:
                self.my_field[b_x][b_y] = 1
                n += 1                            # ув-м кол-во итераций



    def print_field(self):      # функция выводит на экран
        for r in self.my_field: # r - это строка, то есть входим в массив "self.my_field"
            for c in r:         # Далее мы идем по идексу "с" строке
                print(c, end=" ")
            print()



field = Field(10, 10)
field.init_bombs()
field.print_field()
