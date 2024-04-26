import random

class Hangman:
    '''
    A class for the Hangman game.

    ...
    Attributes
    ----------
    word : str
        randomly selected word from word list
    word_guessed : list
        list with same length as selected word, representing word with guessed letters so far
    num_letters: int
        number of unique letters not yet guessed
    num_lives: int
        number of remaining lives
    list_of_guesses: list
        list of letters already guessed

    Methods
    -------
    def check_guess (guess):
        Checks if the letter input by the user is in the randomly selected word.
    '''

    def __init__(self, word_list, num_lives=5):
        '''
        Sets up the necessary attributes for the game.

        Parameters
        ----------
        word : str
            randomly selected word from word list
        word_guessed : list
            list with same length as selected word, representing word with guessed letters so far
        num_letters: int
            number of unique letters not yet guessed
        num_lives: int
            number of remaining lives
        list_of_guesses: list
            list of letters already guessed        
        '''
        
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []                   

    def check_guess (self, guess):
        '''
        Checks if the letter input by the user is in the randomly selected word.
        
        Parameters
        ----------
        guess : the letter being checked

        Returns
        -------
        None
        '''

        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range (len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left')
        return
    
    def ask_for_input(self):
        '''
        Requests input of a letter from the user and validates it, calling the check_guess function to check if it's in the word.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        while True:
            guess = input('Enter a letter: ')
            if len(guess) !=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess.lower() in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess.lower())
            print(f'{self.word_guessed} \t\t Letters guessed so far:', ', '.join(str(x) for x in sorted(self.list_of_guesses)))
            return
    
def play_game(word_list):
    '''
    Creates a game of class Hangman and continues until the user guesses all letters, or their lives run out.

    Parameters
    ----------
    word_list : list
        list of words from which to randomly select word to be guessed
    
    Returns
    -------
    None    
    '''

    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            return
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            return

word_list = ['strawberry','blueberry', 'cherry', 'peach', 'grape']

play_game(word_list)