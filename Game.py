
class Game:
    ''' XO (tic tac toc) game object '''

    def start(self):

        while(self.game_state() == self.enums.Continue_STAT):

            current_player = 0 if (self.turn == self.enums.X) else 1

            move = self.players[current_player].play(self)

            self.grid[move] = self.turn

            self.gameplay.append(move)

            self.turn = self.enums.O if (self.turn == self.enums.X) else self.enums.X

        
        for p in self.players:
            p.done(self)
        


    def game_state(self):
        ''' returns one of the state values in signs.py '''

        # check horizental lines for wins
        for k in range(0,7,3):
            if self.grid[k] and self.grid[k] == self.grid[k+1] and self.grid[k] == self.grid[k+2]:
                return self.grid[k]
        
        # check vertical lines for wins
        for k in range(0,3):
            if self.grid[k] and self.grid[k] == self.grid[k+3] and self.grid[k] == self.grid[k+6]:
                return self.grid[k]

        # check cross lines for wins
        if (self.grid[4]) and (
               (self.grid[4] == self.grid[8] and self.grid[4] == self.grid[0])
               or (self.grid[4] == self.grid[2] and self.grid[4] == self.grid[6])):
            
            return self.grid[4] 

        # check if there is empty squares ( check if game should continue )
        for i in self.grid:
            if not i:
                return self.enums.Continue_STAT 
        
        # return a DRAW state
        return self.enums.DRAW_STAT

# Helping methods ###############################    

    def get_printable_grid(self):
        
        upper_line = "\n_____________\n"
        row_down_borders = "|___|___|___|\n"

        res = upper_line

        for i in range(0,9,3):
            row_str = ( "| " + self.enums.get_sign(self.grid[i]) +
                       " | " +  self.enums.get_sign(self.grid[i+1]) +
                       " | " + self.enums.get_sign(self.grid[i+2]) + " |\n")
            res = res + row_str + row_down_borders

        return res

    def square_full(self, n):
        if self.grid[n]:
            return True
        return False

    

    def __init__(self, player1, player2, enums):

        self.enums = enums

        self.grid = [None]*9

        self.players = [player1, player2]

        self.turn = self.enums.X

        self.gameplay = []
