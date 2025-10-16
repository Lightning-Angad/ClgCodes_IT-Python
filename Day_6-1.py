#Printing Fibonacci-Series using Functions
def fibo (n):
    f0, f1, f = 0, 1, 0
    if n<=0:
        print("Fibonacci Series not possible")
    elif n==1:(
        print ("Fibonacci Series: ", f0))
    else:
        print ("Fibonacci Series: ")
    for i in range (n):
        f0=f1
        f1=f
        f=f0+f1
        print(f, end= " ")
m=int(input("Enter the nth term: "))
fibo(m)
