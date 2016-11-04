from random import randint

a = int(input("Give me a Number: "))
b = int(randint(1,9))

print( "Too High" if a>b else ( "Too Low" if a<b else "Exactly Same"))