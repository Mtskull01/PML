def check_substring(string, substring):
    if substring in string:
        return True
    else:
        return False
string=input("Enter the line of your choice")
substring=input("Enter the substring you want to check:")
if check_substring(string,substring):
    print("Substring found!")
else:
    print("No substring like this.")