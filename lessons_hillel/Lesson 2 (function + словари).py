def show(a):
    for i in range(a):
        print(i)

def show(a, b):
    for i in range(a, b):
        print(i)

def show_while(a):
    i = 0
    while i <= a:
        if i == 5:
            i += 1
            continue

        if i == 450:
            break
        print(i)
        i += 1

#show(10)
#show(11, 20)
#show_while(1000)

#Словари...
contacts = {}

contacts["John"] = 1234567 #"адаm" это как один индекс(ключ, т. е., индекс = ключ
contacts["Adam"] = 74302323
contacts["Oleg"] = 133311313

for name, number in contacts.items():
    print("Phone number of %s is %d" % (name, number))

#или print (contacts["John"]), но не надо тогда цикл for писать



