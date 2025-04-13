import random
secret_number = random.randint(1 , 99)

guess = int(input("I am thingking of a number between 0 and 99...\nEnter a guess:" ))

while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else: 
        print("Your guess is too low")

    guess = int(input("\nEnter a new Number: "))

    print(f"Congrats: The number was: {secret_number}")