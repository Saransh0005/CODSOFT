import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win! 🎉")
    else:
        print("You lose. 😢")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()