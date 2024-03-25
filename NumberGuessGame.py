import random  # Import the random module to generate random numbers

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10  # Set the maximum number of attempts
    
    while attempts < max_attempts:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1  # Increment the attempts counter
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}!")
            break  # Exit the loop if the guess is correct
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    
    # If the player runs out of attempts
    if attempts == max_attempts:
        print(f"\nGame Over! The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
