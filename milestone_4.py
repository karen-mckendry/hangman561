import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))      # no of unique letters not yet guessed
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []                   # list of guesses already tried

    def check_guess (self, guess):
        '''
        This method is used to check if the letter input by the user is in the randomly selected word

        Args:   guess: the letter being checked

        Returns:    None
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range (len(self.word)):
                if self.word[i]==guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left')
    
    def ask_for_input(self):
        '''
        This method takes a letter input by the user and validates it.

        '''
        while True:
            guess = input('Enter a letter: ')
            if len(guess) !=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess.lower() in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    

word_list = ['strawberry','blueberry', 'cherry', 'peach', 'grape']

game1 = Hangman(word_list)
print(game1.word_guessed)
game1.ask_for_input()



