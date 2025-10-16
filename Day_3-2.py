#Searching element in Tuple
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n=int(input("Enter the element to be search: "))
if (n in tuple):
    print ("Present")
else:
    print ("Absent")