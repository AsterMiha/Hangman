import sys
import random

def show_instructions():
	print("")
	print("*"*33)
	print("Guess the word letter by letter\n")
	print("To exit the game type \"exit\"")
	print("To start a new game type \"newgame\"")
	print("To see these instructions again type \"help\"")
	print("*"*33)
	print("")

def does_letter_exist(letter, word):
	if letter in word:
		return True
	return False

# returns a replacement for spaces containing the letters
def put_letter(letter, word, spaces):
	new_spaces = list(spaces)
	for i in range(len(word)):
		if letter==word[i]:
			new_spaces[i*2]=letter
	return "".join(new_spaces)



#get the word choices
filename = raw_input("Teach me some words! (choose a file) ")
try:
	with open(filename) as f:
		lines = f.readlines()
except:
	print("Sorry! Can't read that!")
	sys.exit()

option = ""
word_chosen = lines[random.randint(0, len(lines)-1)].strip().upper()
spaces = len(word_chosen)*"_ " # what the player sees
mistakes = 0
lost_game = 0 # makes the diffe
games_lost = 0
games_won = 0

show_instructions()

while option!="EXIT":
	print(spaces+"	miss:"+str(mistakes))
	option = raw_input("Try a new letter? ").upper()
	
	if len(option)==1:
		if option not in word_chosen:
			mistakes = mistakes+1
		else:
			spaces=put_letter(option, word_chosen, spaces)

	# too many mistakes
	if mistakes>=6:
		print("The word was "+word_chosen.upper())
		lost_game = 1
		games_lost += 1
		option = "NEWGAME"

	# check if the word has been found
	word_found = spaces.replace(" ", "")
	if word_found==word_chosen:
		print(word_chosen)
		print("Found the word!")
		games_won += 1
		option = "NEWGAME"

	if option=="HELP":
		show_instructions()

	# start a new game?
	if option=="NEWGAME":
		option = raw_input("Play again? ").upper()
		if option=="YES": # choose new word
			word_chosen = lines[random.randint(0, len(lines)-1)]
			word_chosen = word_chosen.strip()
			spaces = len(word_chosen)*"_ "
			mistakes = 0
			lost_game = 0
		else: # end the game or resume the previous one
			if lost_game==1:
				option = "EXIT"


# end of the game
print("Won: "+str(games_won))
print("Lost: "+str(games_lost))
print("Bye!")
