
# Signs
X = 11
O = 12

# Game States
X_wins_STAT = 11
O_wins_STAT = 12
DRAW_STAT = 1
Continue_STAT = 0

def get_sign(sign):
    if sign == None:
        return " "
    elif sign == X:
        return "X"
    else:
        return "O"

def get_state(state):

    if state == None:
        return " "
    elif state == X_wins_STAT:
        return "X wins"
    elif state == O_wins_STAT:
        return "O wins"
    elif state == DRAW_STAT:
        return "DRAW"
    else:
        return "Game not done"

