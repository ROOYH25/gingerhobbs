import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it. Good luck!\n")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            print(f"The secret number was {secret_number}!")
            
            # Performance rating
            if attempts <= 3:
                print("Amazing! You're a guessing master!")
            elif attempts <= 6:
                print("Great job!")
            else:
                print("Good work!")
            return
    
    print(f"\nGame over! The secret number was {secret_number}.")
    print("Better luck next time!")

def rock_paper_scissors():
    print("\n" + "="*40)
    print("Welcome to Rock-Paper-Scissors!")
    print("="*40)
    
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        print("Enter 'rock', 'paper', 'scissors', or 'quit' to exit")
        
        user_choice = input("Your choice: ").lower().strip()
        
        if user_choice == 'quit':
            break
        elif user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        # Check for game end
        if user_score >= 3 or computer_score >= 3:
            print("\n" + "="*40)
            if user_score > computer_score:
                print("🎉 Congratulations! You won the game! 🎉")
            else:
                print("💻 Computer wins the game! Better luck next time!")
            print("="*40)
            break

# Main game selector
def main():
    while True:
        print("\n" + "="*50)
        print("🎮 MINI GAME COLLECTION 🎮")
        print("="*50)
        print("1. Number Guessing Game")
        print("2. Rock-Paper-Scissors")
        print("3. Exit")
        
        choice = input("\nSelect a game (1-3): ").strip()
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()