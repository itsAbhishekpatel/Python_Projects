#importing liberary
import random
import time

#create variable 
rock = 1
paper = 2
scissor = 3

# dictionary for rules and name 
names = {rock:"Rock", paper:"Paper", scissor:"Scissor"}
rules = {rock:scissor, paper:rock, scissor: paper}

#variable to track the score
player_score = 0
computer_score = 0

# start func that keep as playing
def start():
    print("Let's play a game of rock, paper, scissor.")
    while game():
        pass
    score()

#define game function find player move and computer also
def game():
    player = move()
    computer = random.randint(1,3)
    result(player,computer)
    return play_again()

# move function take user input
def move():
    while True:
        player = int(input(" Rock = 1\n Paper = 2\n Scissor = 3 \n Make your move: "))
        try:
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! I din't understand that.Please enter 1, 2 or 3.")

# result function to find out who win 
def result(player,computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer through {0}".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie Game.")
    else:
        if rules[player] == computer:
            print("Hurray! You Win")
            player_score += 1
        else:
            print("The Computer laugh as you realise you have been defeated. ")
            computer_score += 1

# play_again function ask user is he/she play again or not
def play_again():
    answer = input("Would you like to play again y/n.")
    if answer in ("y","Y","yes","Yes"):
        return answer
    else:
        print("\nThankyou very much for playing our game. see you next time!")

# score function print score of player and computer
def score():
    global player_score, computer_score
    print("Scores.")
    print("Player: ",player_score)
    print("Computer: ",computer_score)


if __name__ =='__main__':
    start()







