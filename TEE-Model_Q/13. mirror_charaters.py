def mirrorChars(string,k):

	original = 'abcdefghijklmnopqrstuvwxyz'
	reverse = 'zyxwvutsrqponmlkjihgfedcba'
	dictChars = dict(zip(original,reverse))

	prefix = string[0:k-1]
	suffix = string[k-1:]
	mirror = ''

	for i in range(0,len(suffix)):
		mirror = mirror + dictChars[suffix[i]]

	print (prefix+mirror)
		
# Driver program
if __name__ == "__main__":
	string = input("Enter string: ")
	k = int(input("Enter number: "))
	mirrorChars(string,k)
