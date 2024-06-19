#Fibnacci Series
num=int(input("Enter the series number:"))
first_num=0
second_num=1
fibo_series=[]
for i in range(num):
    fibo_series.append(first_num)
    first_num,second_num=second_num,first_num+second_num
print("The first",num,"Fibonacci series numbers are")
print(fibo_series)


