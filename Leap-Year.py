<<<<<<< HEAD
num = int(input("Enter a year: "))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print(num, "is a leap year")
        else:
            print(num, "is not a leap year")
    else:
        print(num, "is a leap year")
=======
import os
num = int (input("Enter a year: "))
if (num%4==0):
 print (num, "is a leap year")
elif (num%100!=0):
 print (num, "is a leap year")
elif(num%400==0):
 print(num, "is a leap year")
>>>>>>> 57690b549c1ea0eaf326fc51953bc5e14f0b2ece
else:
    print(num, "is not a leap year")