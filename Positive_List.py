list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
i,j = 0,0
while(i < len(list1)):
    if list1[i] >= 0:
        print(list1[i], end = " ")
    i+= 1
print()
while(j < len(list2)):
    if list2[j] >= 0:
        print(list2[j], end = " ")
    j+= 1
