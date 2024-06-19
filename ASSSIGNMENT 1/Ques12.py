number=int(input("Enter number of your choice:"))
convrt_num_to_string=str(number)
sum=0
for digits in convrt_num_to_string:
    sum=sum+int(digits)
print("The number of digits in the given number are:",sum)
