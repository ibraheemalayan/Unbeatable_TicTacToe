from players.player import XOPlayer
from enums import No_must_move

class Bot(XOPlayer):
    ''' abstract class for a bot '''

    def __init__(self, sign):
        super().__init__(sign)

    def play(self, game):

        must_move = self.check_must_moves(game)

        if must_move == No_must_move:
            # Think 
            return randrange(9)

        return must_move

    def check_must_moves(self, game):

        return No_must_move
