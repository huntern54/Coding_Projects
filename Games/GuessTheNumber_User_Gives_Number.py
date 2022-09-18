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
        
def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
        
    while feedback != 'c':
        
        # check done because if low and high are the same, the random.randint will break
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)").lower()
        
        # adjusting upper bound if the guess is too high
        if feedback == "h":
            high = guess - 1  
            
        # adjusting lower bound if the guess is too low
        elif feedback == "l":
            low = guess + 1
            
    print(f"Wow the computer guess the number {guess} correctly")
            
computer_guess(1000)
