#Main
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]

for i in a:
	if i in b:
		c.append(i)
		
print(c)
'''

#Extras 1
'''
from random import randint

a = []
for i in range(1, randint(1,9)): a.append(i)

b = []
for i in range(2, randint(1,9)): b.append(i)

c = []
for i in a:
	if i in b:
		c.append(i)
		
print("a is: ", a)
print("b is: ", b)
print(c)
'''

#Extras 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set(a).intersection(b))

print(c)