import random
import string

class Hangman():
    def hangmanBody(self, guesses):
        if guesses == 8:
			print "________      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
			print "|             "

        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|            "
            print "|             "
            print "|             "
            print "|             "

        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|      |      "
            print "|             "
            print "|             "

        elif guesses == 3:
            print "________      "
            print "|      ^      "
            print "|      o      "
            print "|     /|      "
            print "|             "
            print "|             "

        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|     /|\     "
            print "|             "
            print "|             "

        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|      o      "
            print "|     /|\     "
            print "|     /       "
            print "|             "

        else:
            print "________      "
            print "|      |      "
            print "|      ^      "
            print "|     \o/     "
            print "|      |      "
            print "|     / \     "
            print "|             "

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
      #'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def main(secretWord):

    guesses = 8
    lettersGuessed = []
    hangman = Hangman()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangmanBody(guesses)

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = loadWords().lower()
main(secretWord)
