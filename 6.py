#Logic 1
a = list(input("Give me a String: "))

for i in range(0, int(len(a)/2)):
	if a[i] != a[len(a)-i-1]:
		print ("Not a Palindrome")
		break

if i == int(len(a)/2)-1:
	print("Palindrome")


#Logic 2
'''
a = list(input("Give me a String: "))

b = list(a)
a.reverse()
		
if(b == a):
	print(True)
else:
	print(False)
'''