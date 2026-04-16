import random

# word list (you can move this to hangman_words.py)
words = ["apple", "banana", "laptop", "mobile", "bottle"]

# hangman stages (you can move this to hangman_art.py)
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

# choose random word
chosen_word = random.choice(words)
word_length = len(chosen_word)

# create placeholder
display = ["_"] * word_length
print(display)
# game variables
lives = 6
guessed_letters = []
game_over = False

print("🎮 Welcome to Hangman!")

while not game_over:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    # already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        continue

    guessed_letters.append(guess)

    # check guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"'{guess}' is not in the word.")
        lives -= 1

    # show hangman
    print(stages[6 - lives])

    # lose condition
    if lives == 0:
        game_over = True
        print("💀 GAME OVER")
        print(f"The word was: {chosen_word}")

    # win condition
    if "_" not in display:
        game_over = True
        print("🎉 YOU WIN!")