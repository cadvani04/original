# assignment: PA1
# author: Curran Advani
# date: 1/18/2023
# file: hangman.py is a program that simulates the game of hangman
# input: mostly lives, word length, then when it hits a while loop user starts inputting letters
# output: either winning, losing, or starting a new game
from random import choice,random

from random import choice, randint

dictionary_file = "dictionary.txt"  # make a dictionary.txt in the same folder where hangman.py is located

from random import choice, randint


def import_dictionary(filename):
    newdictionaryfile = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []} # setting up dicionary
    max_size = 12
    try:
        with open(filename) as f: #trying to open file to just look at each word individually
            for word in f:
                word = word.strip("\n")
                word = word.strip()
                word = word.upper()
                if (len(word) < 13 and len(word) > 2):
                    newdictionaryfile[len(word)].append(word)

    except Exception:
        print("Error")
    return newdictionaryfile

def get_game_options():
    print("Please choose a size of a word to be guessed [3 - 12, default any size]:")
    try:
        size = int(input())
        if size < 3 or size > 12: #since the options are from 3 to 12 lives
            size = randint(3, 12)
    except:
        size = randint(3, 12)
    print(f"The word size is set to {size}.") #the size is now chosen
    print("Please choose a number of lives [1 - 10, default 5]:")
    try:
        lives = int(input())
        if lives < 1 or lives > 10: #lives limit
            lives = 5
    except:
        lives = 5
    print("You have", lives, "lives.") #lives are chosen
    return (size, lives)


def checkdone(word, hiddenwords):
    return set(word) == set(hiddenwords) #checking if done


def hangmangame(word, lives):
    while True:
        chosen = [] #set up list to collect guesses
        livesnum = [] #set up the format
        for num in range(lives):
            livesnum.append("O")
        underscores = ["__" if c.isalpha() else c for c in word]

        win = False
        hidden = []
        chosenletters = ""
        print("Letters chosen:", chosenletters) #letters chosen string formatted
        print(" ".join(underscores), end=" ")
        print("  lives:", lives, "".join(livesnum))
        while not win:
            guess = input("Please choose a new letter >  \n").upper() #ask for input for letter

            while not guess.isalpha() or not len(guess) == 1: #just in case it isn't a letter
                guess = input("Please choose a new letter >  \n").upper()

            if guess in chosen: # repick
                print("You have already chosen this letter.")
                continue

            chosen.append(guess)
            chosenletters += guess

            if guess in word: #if the guess is right and it's in the word then i have to format it correctly
                hidden.append(str(guess))
                indices = [i for i, c in enumerate(word) if c == guess]
                for index in indices:
                    underscores[index] = guess

                print("You guessed right!")
                print("Letters chosen:", ", ".join(list(chosenletters)))
                print(" ".join(underscores), end=" ")
                print("  lives:", lives, "".join(livesnum))

                if "__" not in underscores:
                    win = True
                    print(f"Congratulations!!! You won! The word is {word}!")
                    return
            elif guess not in word: #if it isn't in the word than do this for formatting and lives
                print("You guessed wrong, you lost one life.")
                lives = lives - 1
                if "O" in livesnum:
                    livesnum[livesnum.index("O")] = "X"
                print("Letters chosen:", ", ".join(list(chosenletters)))
                print(" ".join(underscores), end=" ")
                print("  lives:", lives, "".join(livesnum))

            if lives == 0:
                print(f"You lost! The word is {word}!")
                return


if __name__ == '__main__': #main function to actually start the game
    dictionary = import_dictionary(dictionary_file)
    print("Welcome to the Hangman Game!")
    play_again = 'Y'
    while play_again.upper() == 'Y':
        game = get_game_options() if play_again.upper() == 'Y' else (None, None)
        if game[0] is not None and game[1] is not None:
            size = game[0]
            lives = game[1]
            mylist = dictionary[size]
            word = choice(mylist)
            hangmangame(word, lives)
        play_again = input("Would you like to play again [Y/N]? \n").upper()
        if play_again != 'Y':
            print("Goodbye!")
            break

















