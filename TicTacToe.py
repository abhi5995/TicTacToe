import os
clear = lambda: os.system('cls')

gameData = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def displayBoard():
    print(f'     |     |     ')
    print(f'  {gameData[0]}  |  {gameData[1]}  |  {gameData[2]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {gameData[3]}  |  {gameData[4]}  |  {gameData[5]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {gameData[6]}  |  {gameData[7]}  |  {gameData[8]}  ')
    print(f'     |     |     ')
    
def playerData():
    playerOneName = input('Enter Player 1 Name: ')
    playerOneChoice = ''
    playerTwoChoice = ''
    while playerOneChoice not in ['X','O']:
        playerOneChoice = input(f'Hello {playerOneName}, Please enter your choice (X or O): ')
    playerTwoName = input('Enter Player 2 Name: ')
    playerTwoChoice = 'X' if playerOneChoice == 'O' else 'O'
    return playerOneName,playerOneChoice,playerTwoName,playerTwoChoice

def ifWinner(playerName, playerChoice):
    global gameData
    if gameData[0] == gameData[1] == gameData[2] == playerChoice or gameData[3] == gameData[4] == gameData[5] == playerChoice or gameData[6] == gameData[7] == gameData[8] == playerChoice or gameData[0] == gameData[3] == gameData[6] == playerChoice or gameData[1] == gameData[4] == gameData[7] == playerChoice or gameData[2] == gameData[5] == gameData[8] == playerChoice or gameData[0] == gameData[4] == gameData[8] == playerChoice or gameData[2] == gameData[4] == gameData[6] == playerChoice:
        clear()
        displayBoard()
        print('GAME OVER!')
        print(f'Congratulations,{playerName} Wins!')
        gameData = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        return True
    else:
        return False

def digitValidator(index, playerName, playerChoice):
    if index.isdigit():
        if gameData[int(index) - 1] == ' ':
            gameData[int(index) - 1] = playerChoice
        else:
            index = input(f"Invalid Index {playerName}!, Choose a number (1-9):")
            digitValidator(index, playerName, playerChoice)
    else:
        index = input(f"Invalid Choice {playerName}!, Choose a number (1-9):")
        digitValidator(index, playerName, playerChoice)
        
def gameOn():
    displayBoard()
    playerOneName,playerOneChoice,playerTwoName,playerTwoChoice = playerData()
    player = 1
    while gameData.count(' ') > 0:
        if player == 1:
            playerName = playerOneName
            playerChoice = playerOneChoice
        else:
            playerName = playerTwoName
            playerChoice = playerTwoChoice
        clear()
        displayBoard()
        index = input(f"{playerName}'s Turn, Choose Index (1-9):")
        digitValidator(index, playerName, playerChoice)
        if ifWinner(playerName,playerChoice):
            break
        player = 2 if player == 1 else 1

gameOn()