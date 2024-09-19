import random
import time

#Welcome Message
def welcome_message():
    print("Hi! Welcome to the number guessing game. Pick a number between 1 and 100")
    time.sleep(2)
    print("You will be given a number of chances to guess based on the difficulty level you select.")
    time.sleep(2)

#Ask user to select difficulty level
def difficulty_level():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            return 10, 'Easy'
        elif choice == '2':
            return 5, 'Medium'
        elif choice == '3':
            return 3, 'Hard'
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

#number to be guessed 
def guess_number():
    return random.randint(1, 100)

#Start of game and display of difficulty level selected
def game():
    chances, difficulty = difficulty_level()
    number = guess_number()
    attempts = 0
    start_time = time.time()
    
    print(f"Great! You have selected the difficulty level with {chances} chances.")
    print("Get ready to start the game.")
    time.sleep(2)
    
    while attempts < chances:
        try:
            guess = int(input("What is your guess?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1

      # checking condition of the guess
        if guess < number:
            print("Incorrect! You need to guess higher than", guess)
        elif guess > number:
            print("Incorrect! You need to guess lower than", guess)
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congrats! You guessed the right number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            return attempts, difficulty

  #Quiting of difficulty level if run out of chances
    print(f"Sorry, you've run out of chances. The right number was {number}.")
    return attempts, difficulty

def main():
    Scores = {'Easy': float('inf'), 'Medium': float('inf'), 'Hard': float('inf')}
    
    while True:
        welcome_message()
        attempts, difficulty = game()
        
        #Update High score for selected difficulty
        if attempts < Scores[difficulty]:
            print(f"New high score for  {difficulty} difficulty!")
            Scores[difficulty] = attempts
            
        print("Current High Scores:")
        print(f"Easy: {Scores['Easy']} attempts")
        print(f"Medium: {Scores['Medium']} attempts")
        print(f"Hard: {Scores['Hard']} attempts")

# Ask if user will like to play again 
        play_again = input("Do you want to play again? (yes or no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
