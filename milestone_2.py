import random

word_list = ['strawberry','blueberry', 'cherry', 'peach', 'grape']

# select random word
word = random.choice(word_list)

# Get user to guess letter
guess = input('Enter a letter: ')

# Checks single alphabetical letter
if len(guess) ==1 and guess.isalpha():
    print ('Good guess!')
else:
    print('Oops! That is not a valid input.')