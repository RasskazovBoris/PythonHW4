a = int(input("Введите длину списка №1: "))
array = []
for i in range(a):
    b = int(input ("Введите значение №" + str(i + 1) + ": "))
    array.append(b)

max = 0
for i in range(len(array)):
    if i == len(array) - 1:
        if array[i - 1] + array [i] + array [0] > max:
            max = array[i - 1] + array [i] + array [0]
          
    else:
        if array[i - 1] + array[i] + array[i + 1] > max:
            max = array[i - 1] + array[i] + array[i + 1]
            

print (array)
print (max)