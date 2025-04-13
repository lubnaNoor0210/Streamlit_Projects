
import random # imports module which generate random numbers

NUM_ROUNDS = 5 # creates a constant 5 round game so that it doesnot run forever

# The Game's Main logic

def main():
    print("Welcome to the HIGH-LOW game!")
    print("print('--------------------------------')")

    score = 0  # starts the game from 0. tracks how many score the user makes
    for round_num in range (1, NUM_ROUNDS + 1): # runs the game 5 times so the game doesnt end after 1 guess
        print(f"\nRound {round_num} of {NUM_ROUNDS}")

        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {your_number}")
        guess = input("Do you think your number is HIGHER or LOWER than the computer's? (h/l):").lower()

        if your_number == computer_number:
            print("It's a tie, but the computer wins in this case!")
        elif guess == 'h':
            if your_number > computer_number:
                print("Correct✅. Your number was higher!")
                score =+ 1
            else:
                print("❌ Nope! Your number wasn't higher.")
        elif guess == 'l':
            if your_number < computer_number:
                print("✅ Correct! Your number was lower.")
                score += 1
            else:
                print("❌ Nope! Your number wasn't lower.")
    else:
        print("⚠️ Invalid input! Please enter 'h' or 'l'.")

        print(f"Computer's Number was: {computer_number}")
        print(f"your score: {score}")
       
    print("\nGame Over!")
    print(f"Final Score: {score} out of {NUM_ROUNDS}")

if __name__ == "__main__":
    main()


        

