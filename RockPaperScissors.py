import random
"""
This program allows the user to play a game of rock paper scissors
"""

def rps():
    choices = ['rock','paper','scissors']
    emojis = ['\U0001f918\U0001f3fd','\U0001f4c3','	\u2702']
    print("\nWelcome to Rock Paper Scissors")
    Rounds = input("\nHow many rounds would you like to play? : ")
    rounds = int(Rounds)
    print("Choices: \n 1: Rock\n 2: Paper\n 3: Scissors")
    win = 0
    lose = 0

    for i in range(0,rounds):
        print("\nRound {}".format(i+1))
        rand = random.randint(0,3)
        if rand > 2:
            rand = random.randint(0, 3)
        computerchoice = choices[rand]
        user = input("Enter your choice: ")
        userchoice = int(user)
        #Breaks the loop if user picks anything other than available options
        if userchoice > 3:
            print("That is not a choice")
            break
        print("{}{} VS {}{}".format(choices[userchoice-1],emojis[userchoice-1],computerchoice,emojis[rand]))
    #Round decisions

        #if computer chooses rock
        if computerchoice == choices[0] and userchoice == 3:
            print("You lose")
            lose +=1
        elif computerchoice == choices[0] and userchoice == 2:
            print("You win")
            win +=1

        #if computer chooses paper
        elif computerchoice == choices[1] and userchoice == 1:
            print("You lose")
            lose +=1
        elif computerchoice == choices[1] and userchoice == 3:
            print("You win")
            win += 1

        #if computer chooses scissors
        elif computerchoice == choices[2] and userchoice == 2:
            print("You lose")
            lose +=1
        elif computerchoice == choices[2] and userchoice == 1:
            print("You win")
            win += 1

        #elif computerchoice == int(user) -1:
        else:
            print("You Draw")



    if win >= (rounds/2):
        print("\nConfratulations! You are the winner!")
    else:
        print("\nSorry you lose :(")
    draw = rounds - (win+lose)
    print("\nSCORE:\nWins: {}\nLosses: {}\nDraws: {}".format(win,lose,draw))

    decision = input("\n Play again? \n y = yes\n n = no\n:\t")
    if decision == "y":
        rps()
    else:
        print("\n Thanks for playing\nGoodbye!")

if __name__ == "__main__":
    rps()


