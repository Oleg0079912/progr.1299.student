# Олег Чупилко, ДЗ - Палиндром.
def is_polindrom(word):
    j = len(word)-1
    i = 0

    while i < j:
        if word[i] != word[j]:
            is_polindrom = False
        else:
            is_polindrom = True
        i = i + 1
        j = j - 1
    return is_polindrom

w = input("Enter your word: ")

res = is_polindrom(w)
if res == True:
    print("Is palindrome")
else:
    print("Is not palindrome")
'''


def is_palindrome(word):

    number = len(word)

    my_range = int(number / 2)

    for i in range(my_range):  # Home work v2.1
        number -= 1
        if word[i] != word[number]:
            return False
    return True


my_word = input("Enter your word: ")

result = is_palindrome(my_word)

if result:
    print("Word is palindrome!")
else:
    print("Word if not palindrome!")
    '''

