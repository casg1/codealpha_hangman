import random

words = ["python", "programming", "computer", "science", "machine", "learning"]

guesses_allowed = 6

def choose_word():
    return random.choice(words)

def display_hangman(incorrect_guesses):
    """Displays the hangman visual based on the number of incorrect guesses."""
    stages = [
        """
           --------
           |      |
           |
           |
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
           |
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
           |
        --------
        """
    ]
    return stages[incorrect_guesses]

def play_game():
    word = choose_word()
    word_letters = list('-' * len(word))
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()
    incorrect_guesses = 0

    print("Welcome to Hangman!")

    while incorrect_guesses < guesses_allowed and '-' in word_letters:
        print(display_hangman(incorrect_guesses))
        print("Word to guess: " + " ".join(word_letters))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining guesses: {guesses_allowed - incorrect_guesses}")

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or guess not in alphabet:
                print("Invalid guess. Please enter a single letter.")
            elif guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                break

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_letters[i] = guess
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

    print(display_hangman(incorrect_guesses))
    print("Word to guess: " + " ".join(word_letters))
    if incorrect_guesses == guesses_allowed:
        print(f"You ran out of guesses. The word was: {word}")
    else:
        print("Congratulations! You guessed the word.")

play_game()
