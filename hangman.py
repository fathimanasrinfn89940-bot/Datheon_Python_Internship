import random

words = ["PYTHON", "COMPUTER", "SECURITY", "LAPTOP", "NETWORK"]
secret_word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0

stages = [
    "  +---+\n  |   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n========="
]

print("WELCOME TO HANGMAN!")

while wrong_guesses < 6:
    print(stages[wrong_guesses])
    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print("Word:", display)
    print("Wrong guesses:", wrong_guesses, "/ 6")

    if all(letter in guessed_letters for letter in secret_word):
        print("YOU WIN! Congratulations!")
        break

    guess = input("Guess one letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter only!")
        continue

    if guess in guessed_letters:
        print("Already guessed! Try another letter.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
else:
    print(stages[6])
    print("GAME OVER!")
    print("The word was:", secret_word)