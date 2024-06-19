num=int(input("Enter any number of your choice:"))
fact=1
if num<0:
    print("Factorial is not valid for negative numbers")
else:
    for i in range(1,num+1):
        fact*=i
    print("Factorial of",num,"is",fact)


