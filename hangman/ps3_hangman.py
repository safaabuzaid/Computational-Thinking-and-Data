# Hangman game
#

# -----------------------------------
# Helper code
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Owner/Desktop/MIT_CDS/Python_Problems/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = True
    for l in secretWord:
        x = x and (l in lettersGuessed)      
    return x 



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    result = ""
    for l in secretWord:
        if l in lettersGuessed:
            result += l
        else:
            result += "_ "
    return result
              
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    allLetters = string.ascii_lowercase
    availableLetters = ""
    for i in allLetters:
        if i not in lettersGuessed:
            availableLetters += i
    return (availableLetters)

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    guessesLeft = 8
    lettersGuessed = []
    x = getAvailableLetters(lettersGuessed)
    for i in range (8):
        print ("You have " + str (guessesLeft) + " guesses left.")
        print ("Available letters: " + x)
        letterGuess = input("Please guess a letter: ")

        if letterGuess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))   
            print ("-----------")
            guessesLeft = guessesLeft
            i = i

        elif letterGuess in secretWord:
            lettersGuessed += letterGuess
            x = getAvailableLetters(lettersGuessed)
            print ("Good guess: " + getGuessedWord(secretWord,lettersGuessed))
            print ("-----------")
            i = i
            if getGuessedWord(secretWord,lettersGuessed) == secretWord:
                return ("Congratulations, you won!")

        else: 
            guessesLeft -= 1
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed))
            print ("-----------")
            lettersGuessed += letterGuess
            x = getAvailableLetters(lettersGuessed)

    if getGuessedWord(secretWord,lettersGuessed) != secretWord:
                return ("Sorry, you ran out of guesses. The word was "+ secretWord +".")
        

    #return 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#result = ""
secretWord = chooseWord(wordlist).lower()
print ("Welcome to the game, Hangman!")
print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
print ("-----------")
hangman(secretWord)
