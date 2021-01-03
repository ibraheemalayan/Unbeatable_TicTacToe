from players.player import XOPlayer
from .plans import generate_plans

class Bot(XOPlayer):
    ''' abstract class for a bot '''

    def __init__(self, sign):
        super().__init__(sign)
        self.plans = generate_plans()

    def play(self, game):

        must_move = self.must_move(game)

        if not must_move:
            return self.Think(game)

        return must_move

    def Think(self, game):
        ''' abstract method '''
        print("the Bot.Think was called")


    def must_move(self, game):

        prevent_loss_moves = []

        for line in self.plans['lines']:
            critical_square = self.critical_square_of_line(line, game)
            if critical_square:
            
                if critical_square[1] == game.enums.win_move:
                    return critical_square[0]
                else:
                    prevent_loss_moves.append(critical_square[0])
       
        if len(prevent_loss_moves) > 0:
            return prevent_loss_moves[0]

        # TODO award on multiple prevent loss moves with diffrenet values ( inevitable loss )

        return None
        

    # checks line for must fill squares
    def critical_square_of_line(self, line, game):

        full_squares = []
        empty_square = None
    
        for i in line:
            if game.grid[i]:
                full_squares.append(i)
            else:
                empty_square = i
        
        if len(full_squares) == 2:
            if game.grid[ full_squares[0] ] == game.grid[ full_squares[1] ]:
                
                if game.grid[ full_squares[0] ] == self.sign:
                    return (empty_square, game.enums.win_move)

                return (empty_square, game.enums.prevent_loss_move)
        return None
