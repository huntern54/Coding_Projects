import random

def guess(x):
    
    # create a random number
    random_number = random.randint(1, x)
    
    # initialize guess
    guess = 0
    
    # while loop to iterate with guesses 
    while guess != random_number:
        guess = int(input(f"Guess a random whole number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, that guess is too low. Try again")
        elif guess > random_number:
            print("Sorry that guess is too high. Try again.")

    print(f"Wow how lucky, you guessed the random number: {random_number} correctly ")
        
# input of 10
guess(10)