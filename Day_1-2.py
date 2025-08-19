#Odd-Even Summation
m=int(input("Enter the starting range: "))
n=int(input("Enter the ending range: "))
num=m
print("\nEven Numbers: ")
while num<=n:
    if num%2==0:
        print(num)
    num += 1
num=m
print("\nOdd Numbers: ")
while num<=n:
    if num%2!=0:
        print(num)
    num += 1