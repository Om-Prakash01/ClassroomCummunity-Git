import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!") # Greet the player 
    number_to_guess = random.randint(1, 50)  # pick a random number
    attempts = 0 # keep track of the number of attempts

    while True: # loop until the player guesses correctly
        try:
            user_guess = int(input("Enter your guess (between 1 and 50) : ")) # get the player's guess
            attempts += 1 # increment the attempts counter

            if user_guess <= 0 or user_guess > 50:
                print("Please guess a number within the range of 1 to 50.")
                continue

            if user_guess < number_to_guess:
                print("Too low! Try again.")

            elif user_guess > number_to_guess:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print('Game interrupted by User ')


print(number_guessing_game())