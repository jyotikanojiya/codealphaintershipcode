#hangman game
import random

def select_word():
    words = ["apple", "banana", "orange", "grape", "pear", "kiwi", "strawberry", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = select_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    
    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")
    
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Sorry, that letter is not in the word.")
            guessed_letters.append(guess)
            attempts += 1
            if attempts >= max_attempts:
                print("You've run out of attempts! The word was:", word)
                break

hangman()
