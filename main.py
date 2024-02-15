
import random

def random_number(x):
    return random.randint(1, x)

def check_guess(guess, random_number):
    if guess == random_number:
        return "Correct"
    elif guess < random_number:
        return "Too low"
    else:
        return "Too high"

def guess(x):
    random_number = random_number(x)
    guess = 0
    while check_guess(guess, random_number) != "Correct":
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(check_guess(guess, random_number))
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    while True:
        if low != high:
            guess = random.randint(low, high)
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
            else:
                break
        else:
            guess = low  # could also be high b/c low = high
        print(f'Computer guess: {guess}')
        if feedback == 'c':
            break

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

guess(10)
