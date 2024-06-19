file_name=open("/Users/madhutomar/Library/Mobile Documents/com~apple~TextEdit/Documents/Filling.rtf","w")
text=input("Enter text that you want to write in the file:")
file_name.write(text)
print(file_name)
file_name.close