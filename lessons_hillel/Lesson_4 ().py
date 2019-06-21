#Задача на min and max

class MinMax:

    def __init__(self, arr):
        self.my_arr = arr

    def find_min(self):
        my_min = self.my_arr[0]

        for a in self.my_arr:
            if my_min > a:
                my_min = a

        return my_min

    def find_max(self):
        my_max = self.my_arr[0]

        for a in self.my_arr:
            if my_max > a:
               my_max = a

        return my_max


    arr = [1, 2, 3, 4, 5]
    min_max = MinMax(arr) #object , вызываем...

    print("Min = %d " % min_max.find_min)
    print("Max = %d " % min_max.find_max)



