import random

secret_word = [
    "apple", "banana", "mango", "strawberry",
    "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon",
    "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"
]

word = random.choice(secret_word)

def hangman():
    temp = "_" * len(word)
    print("\n\n")
    print("========   Welcome to Hangman!!   ========")
    print(f"You have {len(word) + 2} attempts to guess the WORD")

    attempts = len(word) + 2

    while attempts > 0:
        print("\n")
        print(f'Attempts left: {attempts}')
        print(temp)

        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            temp = ''.join([guess if word[i] == guess else temp[i] for i in range(len(word))])
            attempts -= 1
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1

        # Check if the player has won
        if temp == word:
            print("######   YOU WON   ######")
            print("Congratulations! You guessed the word correctly.")
            return

    print("######   YOU LOST   ######")
    print(f"The word was: {word}")

hangman()