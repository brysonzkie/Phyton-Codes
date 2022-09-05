secret_number = 2
guessing_count = 0
guessing_limit = 3

while guessing_count < guessing_limit:
    guess = int(input("Guess: "))
    guessing_count += 1
    if guess == secret_number:
        print("You won! ")

else:
    print("Try again")
