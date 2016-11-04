from enum import Enum
Moves = Enum('scissor', 'paper', 'rock')
	

while True:
	p1 = str(input("Player 1: "))
	if p1 in Moves:
		break
	else:
		print("Invalid Option")

while True:
	p2 = input("Player 2: ")
	if p2 in Moves:
		break
	else:
		print("Invalid Option")

