'''
author = 'Patrik Rymel'
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
splitter = '-' * 50

# Necessary variables for user login + greeting users
login = {
	'bob': '123',
	'ann': 'pass123',
	'mike': 'password123',
	'liz': 'pass123'
	}

print(splitter)
print('Welcome to the app. Please log in:')
username = input('USERNAME: ')
password = input('PASSWORD: ')
temp = True

# User login. It runs until user does not enter correct
# name and the given password
while temp:
	if login.get(username) == password:
		print('You are logged in!')
		temp = False
	else:
		print('Bad username or password, you can try again.')
		username = input('Please enter your username: ')
		password = input('Please enter the password: ')

print()
print(splitter)

# Letting user choose from texts, converting it to correct format
print('We have three texts to choose from:')


print(TEXTS[0])
print(splitter)
print(TEXTS[1])
print(splitter)
print(TEXTS[2])

print()

number = int(input('Please choose one text by typing number from 1 to 3: ' )) - 1

print(splitter)

# Deleting all dots and comas from the chosen text; converting the string into a list
text = TEXTS[number]
text = text.replace('.', '')
text = text.replace(',', '')
text = text.split()

# Defining variables for text analysis.
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
total = 0

# Lengths variable is for storing the lengths
# of words, which are actually in the given text.
# It will be used for indexing in length_amount.
lengths = set()
length_amount = {}
words_total = len(text)

# While loop for text analysis
while text:
	word = text.pop()
	length = len(word)
	lengths.add(length)
	length_str = str(length)
	amount = length_amount.get(length_str, 0) + 1
	length_amount[length_str] = amount

	# Conditions are sorted so no type of word is omitted.
	if word.isdigit():
		numeric += 1
		total = total + int(word)
	elif word.islower():
		lowercase += 1
	elif word.isupper():
		uppercase += 1
	elif word.istitle():
		titlecase += 1

print(f'There are {words_total} words in the selected text.')
print(f'There are {titlecase} titlecase words')
print(f'There are {uppercase} uppercase words')
print(f'There are {lowercase} lowercase words.')
print(f'There are {numeric} numeric words.')

print(splitter)

# Sorting the set used for indexing; printing bar "chart"
lengths = sorted(lengths)
while len(lengths) > 0:
	index = str(lengths[0])
	asterisks = '*' * length_amount.get(index)
	print(f'{index} {asterisks} {length_amount.get(index)}')
	lengths = lengths[1:]

print(splitter)

print(f'If we sum all the numbers in this text, we get: {total}')

print(splitter)
