from players.player import XOPlayer
from enums import No_must_move

class Bot(XOPlayer):
    ''' abstract class for a bot '''

    def __init__(self, sign):
        super().__init__(sign)

    def play(self, game):

        must_move = self.check_must_moves(game)

        if must_move == No_must_move:
            return self.think(game)

        return must_move

    def think(self, game):
        ''' abstract method '''

    def check_must_moves(self, game):

        

        return No_must_move
