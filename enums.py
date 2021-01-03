class Enums:

    # Signs
    X = 11
    O = 12
    
    # Game States
    X_wins_STAT = 11
    O_wins_STAT = 12
    DRAW_STAT = 1
    Continue_STAT = 0
    # <Bots land> 
    win_move = 50
    prevent_loss_move = 51
    # </Bots land>
 
    def get_sign(self, sign):
        if sign == None:
            return " "
        elif sign == self.X:
            return "X"
        else:
            return "O"
    
    def get_state(self, state):
    
        if state == None:
            return " "
        elif state == self.X_wins_STAT:
            return "X wins"
        elif state == self.O_wins_STAT:
            return "O wins"
        elif state == self.DRAW_STAT:
            return "DRAW"
        else:
            return "Game not done"
    




