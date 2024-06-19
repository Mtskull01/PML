#Anagram Strings 
def check(s1,s2):
	if(sorted(s1)==sorted(s2)):
		print("The given two strings are anagrams.") 
	else:
		print("Oops!, the given two strings aren't anagrams.")		  
s1 ="astronomer"
s2="moonstarer"
check(s1, s2)
