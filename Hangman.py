import random
import string
from ChosenWords import words

# Find a valid word that is randomized
def GetValidWord(words):
    GuessingWord = random.choice(words)
    
    # Do not choose a word that has a dash or space
    while '-' in GuessingWord or ' ' in GuessingWord:
        GuessingWord = random.choice(words)
        
    # Checks for words in caps 
    return GuessingWord.upper()

def Hangman():
    
    # call to get random word
    GuessingWord = GetValidWord(words)
    # used to keep track as to what has been guessed in the word
    AmountOfLettersInWord = set(GuessingWord)
    alphabet = set(string.ascii_uppercase)
    # keeps track of what user has guessed
    UserGuessedLetters = set()
      
    while len(AmountOfLettersInWord) > 0:
        
        # takes in an iterable and separates between the space 
        print("You have used these letters: ", " ".join(UserGuessedLetters))
        
        # tell what the current word is with a _ as missing letters
        ListOfWords = [letter if letter in UserGuessedLetters else "_" for letter in GuessingWord]
        print("Curent word: ", " ".join(ListOfWords))
        
        UserGuesses = input("Guess a letter: ").upper()
        
        # Take the guess input and store into guessed letters
        # This happens if the user has guessed correctly
        if UserGuesses in alphabet - UserGuessedLetters:
            UserGuessedLetters.add(UserGuesses)
            
            # Remove letter if in the word
            if UserGuesses in AmountOfLettersInWord:
                AmountOfLettersInWord.remove(UserGuesses)
                print("")
        elif UserGuesses in UserGuesses:
            print("You have already guessed that letter. Please guess another.")
        else:
            print("Invalid character")
            
    print(f"Congrats! You successfully guessed the word correctly! The word was: {GuessingWord}\n")
    
Hangman()