# Олег Чупилко, ДЗ - Поиск длинного слова.
def max_word(word):

    my_max = word[0]

    for i in word:
        if len(i) > len(my_max):
            my_max = i
    print(my_max)

word = input().split()
max_word(word)

#Задача -> ... решить по-другому.


def the_longest_word(my_string):
    the_longest_word = 'Hello'

    # TODO: your code here
    return the_longest_word

my_string = "Hello my dear friend"
word = the_longest_word(my_string)
print(word)