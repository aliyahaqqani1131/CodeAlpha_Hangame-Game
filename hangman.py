import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "hangman", "developer", "coding", "program"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words).lower()
    
    # Set maximum allowed incorrect guesses
    max_incorrect_guesses = 6
    incorrect_guesses = 0
    
    # Store guessed letters
    guessed_letters = []
    
    print("=" * 40)
    print("       WELCOME TO THE HANGMAN GAME      ")
    print("=" * 40)
    print(f"Guess the secret word! You have {max_incorrect_guesses} incorrect guesses allowed.\n")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display current word progress (e.g. "_ y t _ o _")
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        current_display = " ".join(display_word)
        print(f"Word: {current_display}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # Check if player has guessed all letters
        if "_" not in display_word:
            print("\n" + "=" * 40)
            print(f"🎉 Congratulations! You guessed the word: '{secret_word}'")
            print("=" * 40)
            break
            
        # Get player input
        guess = input("\nEnter a letter: ").strip().lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetic letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.\n")
            continue
            
        # Add guess to list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")
            
    # Check for game over (loss)
    if incorrect_guesses == max_incorrect_guesses:
        print("=" * 40)
        print("💀 GAME OVER! You ran out of attempts.")
        print(f"The secret word was: '{secret_word}'")
        print("=" * 40)

if __name__ == "__main__":
    play_hangman()
