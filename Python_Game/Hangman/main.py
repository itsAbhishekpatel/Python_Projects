# Hangman game 
from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
        """
        first stage
        """,
        "Second Stage",
        "Third stage",
        "4th ","5th","6th"
    ]

def start():
    print("Lets play a hangman game.")
    while game():
        pass

def game():
    dictionary = ["gru","kernal","magela","ubuntu"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length*["_"]
    tries = 6
    letter_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score,player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letter_tried.find(letter) != -1:
                print("You already picked",letter)
            else:
                letter_tried = letter_tried + letter
                first_index =word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry, letter isn't what we're looking.")
                else:
                    print("Congratulation!",letter,"is correct")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another.")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Guesses",letter_tried)

        if letters_wrong == tries:
            print("Game Over")
            print("The word was",word)
            computer_score += 1
            break

        if "".join(clue) == word:
            print("You win")
            print("The word was",word)
            player_score += 1
            break
    return play_again()

def guess_letter():
    print()
    letter = input("Take a guess at our mystery word:")
    letter.strip()
    letter.strip()
    print()
    return letter

def play_again():
    answer = input("Would you like to play agian? y/n:")
    if answer in ("Y","y","Yes","yes"):
        return answer
    else:
        print("Thank you very much for playing our game. see you next time.")
    
def score():
    global player_score, computer_score
    print( "High Scores")
    print("Player: ",player_score)
    print("Comuter:",computer_score)

if __name__ == '__main__':
    start()

        
    


                







