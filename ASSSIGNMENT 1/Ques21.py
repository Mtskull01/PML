my_list = [1,1,2,2,2,3,3,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6] 
count=0 
element=int(input("Enter the number from the given list, to find its occurence: "))
for i in my_list:
    if i==element:
        count=count+1
print("The occurence of",element,"in the given list is",count)