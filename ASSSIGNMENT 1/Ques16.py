input_string = input("Enter:")
char_freq = {}
for elmnts in input_string:
	if elmnts in char_freq:
		char_freq[elmnts] += 1
	else:
		char_freq[elmnts] = 1

print("Count of all characters in GeeksforGeeks is :\n",str(char_freq))
