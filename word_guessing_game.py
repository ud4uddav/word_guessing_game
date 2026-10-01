# A simple word guessing game for Python beginners.

import random


# Put the possible secret words in a list.
words = ["python", "apple", "tiger", "ocean", "music"]

# random.choice picks one item from the list at random.
secret_word = random.choice(words)

# The player gets six guesses.
guesses_left = 6

print("Welcome to the Word Guessing Game!")
print("Try to guess the secret word.")
print("It has", len(secret_word), "letters.")

# Keep asking for guesses while the player still has guesses left.
while guesses_left > 0:
    guess = input("\nEnter your guess: ").lower()

    # Check that the player entered letters only.
    if not guess.isalpha():
        print("Please enter a word using letters only.")
        continue  # Go back to the beginning of the loop.

    # Compare the guess with the secret word.
    if guess == secret_word:
        print("You won! The secret word was:", secret_word)
        break  # Stop the loop because the game is over.

    # This runs when the guess is not correct.
    guesses_left = guesses_left - 1
    print("Not quite. Guesses left:", guesses_left)

# If all guesses were used, tell the player the answer.
if guesses_left == 0:
    print("Game over! The secret word was:", secret_word)
