#this is merely a proof-of-concept, if I submit this for the final group project I would be flagged for cheating
#this is a Tic Tac Toe AI, the concept being:
#having two list, one for the AI (self) one for the opponent (player), they show all available "wins" each can take
#when either player makes a move, the two list updates, updating all possible "wins" for each player
#when AI is deciding a move, the top priority is making the "highest value play", priority as follows
# 1. If the AI can win (eg. one set in the list only has 1 number left, AI can win instantly by playing it)
# 2. If the player can win (eg. the player can win in next move, AI will take that tile)
# 3. If neither is going to win next move, it would add up all numbers in its list
# making a frequency table, and decide the highest value play base on the frequency

import random

turn = 1
board = {}

winp1 = ['012','345','678','048','147','246','036','258'] #playervalues
winp2 = ['012','345','678','048','147','246','036','258'] #aivalues
value = {}

def update_TTT():
    for i in range(10):
        print("")

    print(" Turn " + str(turn))
    print("----------------")

    for i in range(9):
        if board.get(i) == None:
            print('  .', end = "")
        elif board.get(i) == 1:
            print('  O', end = "")
        elif board.get(i) == 2:
            print("  X", end = "")

        if i == 2 or i == 5 or i == 8:
            print("")

    print("")

def input_phase(player):

    try:
        location = input_translate(int(input("Player " + str(player) + ", Type a Location to Place Your Tile: ")))

        if location < 0 or location > 8:
            update_TTT()
            print("Enter a Valid Number Between 1-9, Try Again")
            input_phase(player)
            return
    except:
        update_TTT()
        print("Enter a Valid Number Between 1-9, Try Again")
        input_phase(player)
        return

    if board.get(location) == None:
        board[int(location)] = player
        update_winlist(str(location), True)
        update_TTT()
    else:
        update_TTT()
        print("Not A Valid Move, Try Again")
        input_phase(player)

#to translate the input on numpad to 0-8 (what the code reads)
def input_translate(input):
    translated = ''
    if input == 7:
        translated = 0
    elif input == 8:
        translated = 1
    elif input == 9:
        translated = 2
    elif input == 4:
        translated = 3
    elif input == 5:
        translated = 4
    elif input == 6:
        translated = 5
    elif input == 1:
        translated = 6
    elif input == 2:
        translated = 7
    elif input == 3:
        translated = 8
    else:
        print("translation error")
        return

    return translated


def check_winner():

    if turn <= 4:
        return

    for i in range(9):
        playernum = board.get(i)

        if playernum == None:
            continue
        elif i == 0:
            if board.get(1) == playernum and board.get(2) == playernum:
                declare_winner(playernum)
            elif board.get(4) == playernum and board.get(8) == playernum:
                declare_winner(playernum)
            elif board.get(3) == playernum and board.get(6) == playernum:
                declare_winner(playernum)
        elif i == 1:
            if board.get(4) == playernum and board.get(7) == playernum:
                declare_winner(playernum)
        elif i == 2:
            if board.get(5) == playernum and board.get(8) == playernum:
                declare_winner(playernum)
            elif board.get(4) == playernum and board.get(6) == playernum:
                declare_winner(playernum)
        elif i == 3:
            if board.get(4) == playernum and board.get(5) == playernum:
                declare_winner(playernum)
        elif i == 6:
            if board.get(7) == playernum and board.get(8) == playernum:
                declare_winner(playernum)

#if its turn 9 already, a winner hasn't been decided, then declares a draw
def check_draw():
    if turn == 9:
        print("the game ends in a draw :(")
        exit()

def declare_winner(player):
    if(player == 1):
        print("Winner is Player" + str(player) + "!")
    else:
        print("Winner is AI~ better luck next time~")
    exit()

def input_ai():

    location = ai_decision()

    if board.get(location) == None:
        board[int(location)] = 2
        update_winlist(location=str(location), player=False)
        update_TTT()
    else:
        print("error")

def ai_decision():

    #calculate whether a win is available
    for w in winp2:
        if len(w) == 1:
            print("winning move found! Playing it at " + w)
            return int(w)
    #calculate whether opponent is about to win
    for w in winp1:
        if len(w) == 1:
            print("player about to win! blocking it at " + w)
            return int(w)

    #if above neither happens, go for the highest value play
    return calculate_value()

def calculate_value():
    #loop along the list of winp2, record in the dictionary for the frequency of every number
    value = {}
    for w in winp2:
        for c in w:
            if value.get(c) != None:
                value[c] += 1
            else:
                value[c] = 1

    #after calculating value, creates a list of keys with the highest value, and choose a random one of them
    maxvalue = max(value.values())
    listoftiles = []
    for k in value:
        if value[k] == maxvalue:
            listoftiles.append(k)
    return listoftiles[random.randint(0, len(listoftiles)-1)]

def update_winlist(location, player = True):
    #when player plays a move, update winp1
    if player:
        for i, w in enumerate(winp1):
            winp1[i] = winp1[i].replace(location, '')
        for i, w in enumerate(winp2):
            if w.find(str(location)) != -1:
                print('contains ' + location + " at " + str(w.find(location)))
                winp2[i] = ''
    else:
        for i, w in enumerate(winp2):
            winp2[i] = winp2[i].replace(location, '')
        for i, w in enumerate(winp1):
            if w.find(str(location)) != -1:
                print('contains ' + location + " at " + str(w.find(location)))
                winp1[i] = ''


update_TTT()

while True:
    for i in range(2):

        if i == 0:
            input_phase(1)
        else:
            input_ai()

        check_winner()
        check_draw()
        turn += 1
