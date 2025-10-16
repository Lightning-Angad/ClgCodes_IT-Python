#Searching using Dictionary
dictx={"name":"Sayan", "job":"business", "age":20}
n=input("Enter the key: ")
flag=0
for i in dictx:
    if n in dictx.keys():
        flag=1
if(flag==1):
    print(n, "is found and it's value is", dictx.get(n))
else:
    print(n, "is not found")
    