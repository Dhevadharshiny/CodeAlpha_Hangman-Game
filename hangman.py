import random


def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        """
    ]
    return stages[attempts]
def play_hangman():
    word_list = ["portfolio", "game", "coding", "python", "java"]
    secret_word = random.choice(word_list)
    display_word = ["_"] * len(secret_word)
    attempts = 6  
    guessed_letters = set()
    print("Welcome to Hangman!") 
    while attempts > 0 and "_" in display_word:
        print(display_hangman(attempts))  
        print("\nWord:", " ".join(display_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed this letter!")
            continue
        guessed_letters.add(guess)
        if guess in secret_word:
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print(display_hangman(attempts))  
        print("\nGame over! The correct word was:", secret_word)
if __name__ == "__main__":
    play_hangman()
