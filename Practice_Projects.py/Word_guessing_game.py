import random

def word_guessing_game():  
    user_name = input("Enter your name: ")  # ask the user name
    print(f"Welcome to the Word Guessing Game and Good luck, {user_name}!")  # greet the user

    # list of words
    words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 
             'genius', 'player', 'condition', 'reverse', 'water', 'board', 'geeks', 
             'sweet', 'beautiful']

    word = random.choice(words)  # pick a random word

    print(f"Guess the word from this list:\n{words}")

    attempts = 5  # number of attempts user have.

    try:
        while attempts > 0:
            guess = input("Enter your guess: ").lower().strip()

            # Handle boundary cases
            if not guess:  # empty input
                print("Please enter a word!")
                continue

            if not guess.isalpha(): # non-alphabetic input
                print("please enter a valid word containing only letters!")
                continue

            if guess not in words:  # check if guess is in the list
                print("That word is not in the given list!")
                continue

            if guess == word:  # correct guess
                print("You Win!")
                print(f"The word is: {word}🎆🎊")
                break
            else:  # wrong guess
                attempts -= 1
                print("Wrong guess!🥲")
                print(f"You have {attempts} more attempts")

                if attempts == 0:
                    print("You Lose 😂")
                    print(f"The correct word was: {word}")

    except KeyboardInterrupt:
        print("\nGame interrupted by user. Goodbye!") # when user presses ctrl+C for forcefully stop the program.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    word_guessing_game()
