import random

secret = random.randint(1, 30)
attempts = 0

with open("attempts.txt") as score_file:
    best_score = int(score_file.read())
    print("Top score:", best_score)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed:", attempts)
        if attempts < best_score:
            with open("attempts.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Sorry, too high")
    elif guess < secret:
        print("Sorry, too low")