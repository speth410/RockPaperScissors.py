#Nicholas Speth
#FinalProject.py
#COP 1000
#This program is a simple text based implementation of Rock, Paper, Scissors
#in the Python programming language

from random import randint

ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
    #Declare and initialize variables
    menuInput = 0
    playerOneWeapon = 0
    playerTwoWeapon = 0
    playerOneScore = 0
    playerTwoScore = 0
    gamesPlayed = 0
    keepOpen = True

    #Keep game open until user chooses to EXIT
    while keepOpen == True:
        #Function Calls
        menuInput = mainMenu()
        
        if menuInput == 1:
            gameRules()

        elif menuInput == 2:
            playerOneWeapon, playerTwoWeapon, gamesPlayed = singlePlayer(gamesPlayed)
            playerOneScore, playerTwoScore = findWinner(playerOneWeapon, playerTwoWeapon, playerOneScore, playerTwoScore)
            displayScore(playerOneScore, playerTwoScore, gamesPlayed)

        elif menuInput == 3:
            playerOneWeapon, playerTwoWeapon, gamesPlayed = twoPlayer(gamesPlayed)
            playerOneScore, playerTwoScore = findWinner(playerOneWeapon, playerTwoWeapon, playerOneScore, playerTwoScore)
            displayScore(playerOneScore, playerTwoScore, gamesPlayed)

        elif menuInput == 4:
            keepOpen = False
            
def mainMenu():
    menuInput = 0
    goodInput = False

    #The main menu will be displayed until a valid input is recieved
    while goodInput == False:
        print("\n\nRock, Paper, Scissors")
        print("_________________________\n")
        print("1: See the rules")
        print("2: Play against the computer")
        print("3: Play a two player game")
        print("4: QUIT")
        
        menuInput = int(input("\nEnter 1-4: "))

        #Check to make sure the user entered a number 1-4
        goodInput = checkInput(menuInput)
        
    return menuInput

def gameRules():

    #Display game rules to the user
    print("\n\tGame Rules")
    print("______________________________\n")
    print("Paper Covers Rock")
    print("Rock Smashes Scissors")
    print("Scissors Cut Paper\n")

    #Allows users to read the rules before returning to the main menu.
    input("Press ENTER to return to the Main Menu: ")
    
def weaponMenu():
    weaponInput = 0
    goodInput = False

    #Display weapons menu until a valid input is recieved.
    while goodInput == False:
        print("\n\tChoose Your Weapon!")
        print("______________________________\n")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")
        print("4: Return To Main Menu")
        
        weaponInput = int(input("Enter 1-4: "))

        #Check to make sure the user entered a number 1-4
        goodInput = checkInput(weaponInput)
        
    return weaponInput
    
def checkInput(userInput):
    #If user entered a number 1-4 continue running
    if userInput > 0 and userInput <= 4:
        goodInput = True
        return goodInput
        
    else:
        #Menu is displayed again
        print("\nINVALID INPUT\n")
        goodInput = False
        
def singlePlayer(gamesPlayed):
    userWeapon = 0
    computerWeapon = 0

    gamesPlayed = gamesPlayed + 1

    #User picks their weapon using the weapons menu
    userWeapon = weaponMenu()
    #Computer uses randint() to choose a random number 1-3
    computerWeapon = randint(1,3)

    #findWinner determines the winner based on both weapon choices
    return userWeapon, computerWeapon, gamesPlayed
 
def twoPlayer(gamesPlayed):
    playerOneWeapon = 0
    playerTwoWeapon = 0

    gamesPlayed = gamesPlayed + 1

    #Both players pick their weapons using the weapons menu
    playerOneWeapon = weaponMenu()
    playerTwoWeapon = weaponMenu()

    #findWinner determines the winner based on both weapon choices
    return playerOneWeapon, playerTwoWeapon, gamesPlayed
    
def findWinner(playerOne, playerTwo, playerOneScore, playerTwoScore):
    #If both picked the same weapon
    if playerOne == playerTwo:
        print("It's a tie!")

    #If Player 1 picked rock
    elif playerOne == ROCK:
        if playerTwo == SCISSORS:
            print("Player One Wins! Rock Smashed Scissors")
            playerOneScore = playerOneScore + 1
        else: #Paper
            print("Player Two Wins! Paper Covers Rock")
            playerTwoScore = playerTwoScore + 1

    #If Player 1 picked paper
    elif playerOne == PAPER:
        if playerTwo == ROCK:
            print("Player One Wins! Paper Covers Rock")
            playerOneScore = playerOneScore + 1
        else: #Scissors
            print("Player Two Wins! Scissors Cut Paper")
            playerTwoScore = playerTwoScore + 1

    #If Player 1 picked scissors
    elif playerOne == SCISSORS:
        if playerTwo == PAPER:
            print("Player One Wins! Scissors Cut Paper")
            playerOneScore = playerOneScore + 1
        else: #Rock
            print("Player Two Wins! Rock Smashed Scissors")
            playerTwoScore = playerTwoScore + 1

    return playerOneScore, playerTwoScore

def displayScore(playerOneScore, playerTwoScore, gamesPlayed):

    print("\n\t\tSCORE")
    print("_________________________\n")
    print("Player One  |  Player Two")
    print("\t", playerOneScore, "\t\t|\t", playerTwoScore)
    print("_________________________\n")
    print("Games Played: ", gamesPlayed)


main()
 
 
    
