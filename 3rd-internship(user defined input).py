
#1.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
print("\nPython program to calculate the product, multiplying all the numbers in a given tuple.")
tup=tuple()
while True:
    x=int(input("Enter number"))
    tup+=(x,)
    if (ch:=input("Enter exit to stop")).lower()=="exit":
        break
print("Input is:",tup)
product=1
for i in tup:
    product*=i
print("Product is:",product)

#2.Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
print("\nPython program to calculate the average value of the numbers in a given tuple of tuples.")
tup,maint,out=tuple(),tuple(),tuple()
num=int(input("Enter no of values in each tuple"))
while True:
    for i in range(num):
        x=int(input("Enter number"))
        tup+=(x,)
    maint+=(tup,)
    print("Recently entered tuple is:",tup)
    tup=()
    if (ch:=input("Enter exit to stop input")).lower()=="exit":
        break
print("Input is:",maint)
l=[]
x=len(maint[0])
for j in range(x):
    sum=0
    for k in range(len(maint)):
        sum+=maint[k][j]
    avg=sum/len(maint)
    l+=[avg]
print("The average is",tuple(l))
    
