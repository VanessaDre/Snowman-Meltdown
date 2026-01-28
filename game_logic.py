import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the guessed word progress."""
    mistakes = min(mistakes, len(STAGES) - 1)
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Guessed:", " ".join(guessed_letters) if guessed_letters else "-")
    print()

def ask_replay():
    answer = input("Play again? (y/n): ").lower().strip()
    return answer == "y"


def play_game():
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("Welcome to Snowman Meltdown!")

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print("🎉 You saved the snowman! The word was:", secret_word)
                break

            if mistakes >= max_mistakes:
                print("💧 The snowman melted... The word was:", secret_word)
                break

            guess = input("Guess a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter (a-z).")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            if guess in secret_word:
                guessed_letters.append(guess)
                print("✅ Correct!")
            else:
                mistakes += 1
                print("❌ Wrong!")

        if not ask_replay():
            print("Bye! 👋")
            break
