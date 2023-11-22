import random

word_list = ['strawberry','blueberry', 'cherry', 'peach', 'grape']

# select random word
word = random.choice(word_list)

# check if guessed letter is in word
def check_guess (guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

# Get user to guess a letter and check it is a single alphabetical letter
def ask_for_input():
    while True:
        guess = input('Enter a letter: ')
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()

