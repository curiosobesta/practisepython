a = int(input("Give me a number: "))
l=[]
for i in range(1,a+1):
	if a%i==0:
		l.append(i)

print (l)