### IMPORT ###
import os

### FUNCTIONS ###
# Clean windows and print application header
def show_title():
	os.system('cls')
	print("\t**************************************")
	print("\t************** MAD LIBS **************")
	print("\t**************************************")

# Print options available and get an input
def get_choice():
	print("\n[1] Play.")
	print("[q] Quit.")
	
	return input("\nWhat would you like to do? ")

# Get four different word inputs and print them in
# a  Mad Lib setence
def get_words():
	exclamation = ''
	exclamation = input("\nPlease enter an exclamation: ")
	adverb = ''
	adverb = input("\nPlase enter an adverb: ")
	noum = ''
	noun = input("\nPlease enter a noun: ")
	adjective = ''
	adjective = input("\nPlease enter an adjective: ")
	
	return print("\n%s! He said %s as he jumped into his convertible %s"
	" and drove off with his %s wife." % (exclamation.upper(), adverb, noum,
	adjective))
	
### MAIN CODE ###
# Create choice variable
choice = ''
show_title()

# Run application while input is not 'q'
while choice != 'q':
	choice = get_choice()
	
	show_title()
	
	if choice == '1':
		get_words()
	elif choice == 'q':
		print("\nOk, thanks for playing.")
	else:
		print("\nI don't know this command, sorry.")
