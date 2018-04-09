import random
import string

WORDLIST_FILENAME = "palavras.txt"

class WordWorld(object):
    def __init__(self, guesses):
        self.secret_word = self.load_words().lower()
        self.letters_guessed = []
        self.guessed = guesses
    
    def is_word_guessed(self):
        # secret_letters = []

    #    for letter in secret_word:
    #        if letter in secret_letters:
    #            secret_letters.append(letter)
    #        else:
    #            pass

        for letter in self.secret_word:
          if letter in self.letters_guessed:
            pass
          else:
            return False

        return True
    def load_words(self):
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

class Hangman(WordWorld):
    def hangman_body(self, guesses):
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

def get_guessed_word():

     guessed = ''


     return guessed

def get_available_letters():
    import string
      #'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def main():

    guesses = 8
    letters_guessed = []
    hangman = Hangman(guesses)

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(hangman.secret_word), ' letters long.'
    print '-------------'

    while  hangman.is_word_guessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangman_body(guesses)

        available = get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:

            guessed = get_guessed_word()
            for letter in hangman.secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in hangman.secret_word:
            letters_guessed.append(letter)

            guessed = get_guessed_word()
            for letter in hangman.secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)

            guessed = get_guessed_word()
            for letter in hangman.secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if hangman.is_word_guessed() == True:
            hangman.hangman_body(guesses)
            print 'Congratulations, you won!'
        else:
            hangman.hangman_body(guesses)
            print 'Sorry, you ran out of guesses. The word was ', hangman.secret_word, '.'


main()
