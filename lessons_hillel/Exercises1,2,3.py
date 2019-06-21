# Exercise 2
numbers = []
strings = []
names = ["John", "Erica", "Jessica"]

# Codding
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("привет")
strings.append("иир")

second_name = 0
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Exercise 3
x = object()
y = object()

x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_list = [1, 67, 3, 4, 5, 6, 7, 8, 9, 10]

big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# Exercise 4
data = ("John", "Doe", 53.44)
fornat_string = "Hello"

print(fornat_string % data)




