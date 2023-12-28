import string
import random

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word

def get_available_letters(letters_guessed):
    letters = list(string.ascii_lowercase)
    for letter in letters:
        if letter in letters_guessed:
            letters.remove(letter)
    return ' '.join(letters)
    
words = open('words.txt','r')
line = words.readline()
wordlist = line.split()
secret_word = random.choice(wordlist)
tries = len(secret_word) + 5
letters_guessed = []

while tries > 0 and not is_word_guessed(secret_word,letters_guessed):
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(get_guessed_word(secret_word, letters_guessed))
    print(get_available_letters(letters_guessed))
    tries -= 1
if is_word_guessed(secret_word, letters_guessed):
    print("Congratulations! You have solved the puzzle")
else:
    print("Better luck next time! The word was:", secret_word)
    