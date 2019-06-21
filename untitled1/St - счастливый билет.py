'''Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство
сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.'''

a1 = int(input())
sum_1 = 0
sum_2 = 0
sum_1 = sum_1 + a1 % 10 + int(a1 % 100 / 10) + int(a1 % 1000 / 100)
sum_2 = int(sum_2 + a1 % 10000 / 1000) + int(sum_2 + a1 % 100000 / 10000) + int(sum_2 + a1 % 1000000 / 100000)

if sum_1 == sum_2:
    print("Счастливый")
else:
    print("Обычный")