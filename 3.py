#Main
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
	if i<5:
		print(i)	
'''

#Extras 1
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
	if i<5:
		b.append(i)
		
print (b);
'''

#Extras 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in a: if i<5: print i
print (for i in a if i<5)