import random


words_and_hints = [
    ("variable", "Used to store data in a program."),
    ("function", "Reusable block of code that performs a task."),
    ("loop", "Used to repeat a block of code."),
    ("dictionary", "Stores data in key-value pairs."),
    ("tuple", "An immutable sequence type."),
    ("indentation", "Used to define code blocks in Python."),
    ("exception", "Raised when an error occurs."),
    ("recursion", "A function calling itself."),
    ("lambda", "Anonymous function in Python."),
    ("iterator", "Used to iterate through objects.")
]



def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]

# Function to play the game
def play_game(word, hint):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print("Let's play Hangman!")
    print(f"Hint: {hint}")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Invalid guess. Please guess a letter or the full word.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print(f"Congratulations! You guessed the word {word}!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")


word, hint = random.choice(words_and_hints)
play_game(word, hint)
while input("Play Again? (Y/N) ").upper() == "Y":
    word, hint = random.choice(words_and_hints)
    play_game(word, hint)
