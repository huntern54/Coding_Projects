import random

def play():
    user = input("'r' for rock, 'p' for paper, 's for scissors' \n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return print("You tied! Computer chose: {computer}\n")
    elif isWin(user, computer):
        return print("You Won! Computer chose: {computer}\n")
    else:
        return print(f"You lost! Computer chose: {computer}")
        
# method to check if user has won
def isWin(player, opponent):
    # r > s , 
    # s > p ,
    # p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

# play 10 times
for i in range(0, 10):
    play()
    
