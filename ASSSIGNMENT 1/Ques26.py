test_str=input("Enter:")
str_start=input("Enter the char to check if the string starts with it or not:")
str_end=input("Enter the char to check if the string ends with it or not:")
# Check if the string starts with the specified character
if test_str.startswith(str_start):
    print("The string starts with the specified character.")
else:
    print("The string does not start with the specified character.")

# Check if the string ends with the specified character
if test_str.endswith(str_end):
    print("The string ends with the specified character.")
else:
    print("The string does not end with the specified character.")