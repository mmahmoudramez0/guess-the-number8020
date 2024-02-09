import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0  # Added to track the number of attempts
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        attempts += 1  # Increment attempts after each guess
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats! You guessed the number {random_number} correctly in {attempts} attempts.')

def computer_guess(x):
    low = 1
    high = x
    attempts = 0  # Added to track the number of attempts
    while low <= high:  # Improved condition to handle edge cases
        guess = random.randint(low, high)
        attempts += 1  # Increment attempts after each guess
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly in {attempts} attempts!')

guess(10)
