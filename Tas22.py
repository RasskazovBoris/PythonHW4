a = int(input("Введите длину списка №1: "))
array1 = []
for i in range(a):
    c = int(input ("Введите значение №" + str(i + 1) + ": "))
    array1.append(c)
b = int(input("Введите длину списка №2: "))
array2 = []
for i in range(b):
    c = int(input ("Введите значение №" + str(i + 1) + ": "))
    array2.append(c)


finalArray = []
for i in range(len(array1)):
    for j in range (len(array2)):
        if array1[i] == array2[j]:
            finalArray.append(array1[i])

for i in range (len(finalArray)):
    k = i + 1
    while k < len(finalArray):
        if finalArray[i] == finalArray[k]:
            finalArray.__delitem__(k)
        else:
            k = k + 1

print (sorted(finalArray))