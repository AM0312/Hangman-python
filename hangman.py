import random
import os
from _art import stages, logo
from _words import word_list
lives = 6
print(logo)
word = random.choice(word_list)
guess_word = len(word)*["_"]
print(guess_word)
guesses = []
while True:
    guess = input("Guess a letter: ")
    if guess in guesses:
        print("You already guessed this letter.")
        continue
    guesses.append(guess)
    for i in range(len(word)):
        if word[i] == guess:
            guess_word[i] = word[i]
    if guess not in word:
        lives -= 1
        print(stages[lives])
    print(guess_word)
    if guess_word.count("_") == 0:
        print("You won.")
        break
    if lives == 0:
        print("You Lose.")
        print(f"The word was {word}.")
        break
