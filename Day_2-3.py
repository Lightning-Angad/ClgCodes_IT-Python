#Duplicate in List
list=[1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]
print(list)
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
x=unique_list
print(x)