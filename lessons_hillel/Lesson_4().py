#OOP
'''class MyClass:
    variable = "OOP"

    def my_functiion(self):
        print("This is a massege inside the class:")

my_object = MyClass() # создаем обьект классам. Именно чеrез обьект класса мі можем получить доступ к его свойставм

print(my_object.variable)
my_object.my_functiion()

'''
class Person:
    age = 10
    name = "John"
    gender = 1

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show_personal_data(self):
        print("Name: %s, Age: %d" % (self.name, self.age)) #получить доступ к переменным через селф,

# все то мы создлаи анкету

p1 = Person("Mike", 20)
p1.show_personal_data()

p2 = Person("Liza", 22)
#p2.name = "Liza"
#p2.age = 22
p2.show_personal_data()

