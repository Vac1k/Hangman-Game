# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ''
    for i in secret_word:
        if i in letters_guessed:
            word += i
            if word == secret_word:
                return True
        else:
            return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ""
    for i in secret_word:
        if i in letters_guessed:
            word = word+i
        else:
            word = word+"_"
    return word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    available_letters = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in available_letters:
            available_letters.remove(i)
    return "".join(available_letters)

def check_enter(letter,warnings,letters_guessed):
    if len(letter)!=1:
        warnings -= 1
        print("This is not valid letter")
        if warnings<1:
            print("You have no warnings left so you lose one guess: ")
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            print("You have",warnings,"warnings left")
            print(get_guessed_word(secret_word, letters_guessed))
        return True
    elif not letter.isalpha():
        warnings -= 1
        print("This is not valid letter")
        if warnings < 1:
            print("You have no warnings left so you lose one guess: ")
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            print("You have", warnings, "warnings left")
            print(get_guessed_word(secret_word, letters_guessed))
        return True
    elif letter in letters_guessed:
        warnings -= 1
        print("This is not valid letter")
        if warnings < 1:
            print("You have no warnings left so you lose one guess: ")
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            print("You have", warnings, "warnings left")
            print(get_guessed_word(secret_word, letters_guessed))
        return True
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses = 6
    warnings = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is:",len(secret_word)," letters long")
    print('You have ' + str(warnings) + ' warnings left.')
    print("_"*20)
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if len(letter)==1 and letter.isalpha() and letter not in letters_guessed:
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Good guess :", get_guessed_word(secret_word,letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses-=1
        else:
            print("That is not valid letter. ")
            warnings -= 1
            if warnings < 1:
                print(get_guessed_word(secret_word, letters_guessed))
                guesses-=1
            else:
                print("You have", warnings, "warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
    if is_word_guessed(secret_word, letters_guessed):
        print(
            "Congratulations, you won!\n"
            "Your total score for this game is:"
            f"{len(set(secret_word)) * guesses}"
        )
    else:
        print(
            "GAME OVER!\n"
            "Try your luck in the next game.\n"
            f"Your word was {secret_word}"
        )
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word_ = my_word.replace(" ", "")
    list1 = list(my_word_)
    if len(other_word) == len(my_word_):
        for i in range(len(my_word_)):
            if my_word_[i] == other_word[i]:
                continue
            elif my_word_[i] == "_" and other_word[i] not in list1:
                continue
            else:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = ''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches += word
            matches += ' '
    if matches == '':
        print('No matches found.')
    else:
        print('Possible word matches are: ' + str(matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses = 6
    warnings = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is:", len(secret_word), " letters long")
    print("_" * 20)
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if len(letter) == 1 and letter.isalpha() and letter not in letters_guessed or letter=='*':
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Good guess :", get_guessed_word(secret_word, letters_guessed))
            elif letter=='*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
        else:
            print("That is not valid letter. ")
            warnings -= 1
            if warnings < 1:
                print(get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
            else:
                print("You have", warnings, "warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
    if is_word_guessed(secret_word, letters_guessed):
        print(
            "Congratulations, you won!\n"
            "Your total score for this game is:"
            f"{len(set(secret_word)) * guesses}"
        )
    else:
        print(
            "GAME OVER!\n"
            "Try your luck in the next game.\n"
            f"Your word was {secret_word}"
        )


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

  #  secret_word = choose_word(wordlist)
  #  hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

 secret_word = choose_word(wordlist)
 hangman_with_hints(secret_word)