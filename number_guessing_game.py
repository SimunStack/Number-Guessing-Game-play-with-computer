import random

while True:
    print("Choose an option:")
    print("1. You guess the number (computer selects)")
    print("2. Computer guesses your number")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("Computer is thinking of a number between 1 and 100.")
        number = random.randint(1, 100)
        tries = 0
        guess = input("Guess the number (1 to 100): ")
        while True:
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Your guess should be between 1 and 100.")
                continue

            tries += 1

            if guess < number:
                print("Too low!")
                guess = input("Guess again: ")
            elif guess > number:
                print("Too high!")
                guess = input("Guess again: ")
            else:
                print(f"Correct! The Number was {guess}.")
                break

    elif choice == "2":
        secret = input("Think of a number between 1 and 100 and enter it (for test): ")

        if not secret.isdigit():
            print("Please enter a valid number next time.")
            continue

        secret = int(secret)
        if secret < 1 or secret > 100:
            print("Number must be between 1 and 100.")
            continue

        low = 1
        high = 100
        tries = 0

        while True:
            if low > high:
                print("Something's wrong. Let's try again.")
                break

            guess = (low + high) // 2
            tries += 1
            print(f"Computer guesses: {guess}")
            feedback = input("Your feedback (H/L/C) ").upper()

            if feedback not in ['H', 'L', 'C']:
                print("Please enter H, L, or C.")
                continue

            if feedback == 'C':
                print(f"Computer guessed your number in {tries} tries!")
                break
            elif feedback == 'H':
                high = guess - 1
            elif feedback == 'L':
                low = guess + 1

    elif choice == "3":
        print("Goodluck!")
        break

