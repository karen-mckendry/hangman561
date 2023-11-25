# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Table of Contents

-  Description
-  Installation
-  Usage
-  License

## Description

This is a fruity version of the Hangman game, where a user has to guess which fruit the computer has randomly selected from a list of 5 fruits. The user inputs a letter, and once confirming the input is valid and hasn't already been guessed, the game checks whether the letter is contained within the randomly selected word. If it is, the letter is recorded in each of the positions in the guessed word where it appears in the selected word. And if not, the user receives a message and is prompted to try again. Users have 5 lives, which reduce by 1 with each incorrect guess.

Development of the game started with defining the word list and using the choice method of Python's random module to select one at random. The user is asked for input which is validated to ensure the length = 1 and the input is alphabetical using the isalpha() method. Next, this was put inside a function, and another function was defined to check if the guess was in the word, having converted it to lower case. In the following stage, a class was defined and some attributes initialised: the randomly chosen word, the guessed word, the number of unique letters not yet guessed, how many lives remain, the list of possible words and the list of letters already guessed. The functions were moved inside the class and enhanced to update the guessed word with correctly guessed letters, and to adjust to the number of lives and the list of guessed letters.

## Installation

git clone https://github.com/karen-mckendry/hangman561

## Usage

## License




