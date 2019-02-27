import sys
import random

def show_instructions():
	print("")
	print("*"*33)
	print("TODO - instructions")
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
word_chosen = lines[random.randint(0, len(lines)-1)].strip()
spaces = len(word_chosen)*"_ " # what the player sees
mistakes = 0

while option!="exit":
	print(spaces+"	miss:"+str(mistakes))
	option = raw_input("Try a new letter? ").lower()
	
	if len(option)==1:
		if option not in word_chosen:
			mistakes = mistakes+1
		else:
			spaces=put_letter(option, word_chosen, spaces)

	# too many mistakes
	if mistakes>=5:
		print("The word was "+word_chosen)
		option = "newgame"

	# check if the word has been found
	word_found = spaces.replace(" ", "")
	if word_found==word_chosen:
		print("Found the word!")
		option = "newgame"

	if option=="help":
		show_instructions()

	# start a new game?
	if option=="newgame":
		option = raw_input("Play again? ").lower()
		print(option)
		if option=="yes": # choose new word
			word_chosen = lines[random.randint(0, len(lines)-1)]
			word_chosen = word_chosen.strip()
			spaces = len(word_chosen)*"_ "
			mistakes = 0
		else: # end the game
			option = "exit"


# end of the game
print("Bye!")
