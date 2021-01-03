from .bot import Bot
from random import randint

class Rand_Bot(Bot):
    ''' stupid bot that plays randomly '''

    def __init__(self, sign):
        super().__init__(sign)

    # overrides the default behaviour of checking for "must moves"
    # because this bot should be completely random
    def play(self, game):
        return self.think(game)

    # overrides the super method
    def think(self, game):

        empty_squares = []
        
        # check for empty square
        i = 0
        while(i<9):
            if not game.square_full(i):
                empty_squares.append(i)
            i += 1
        
        # choose a random empty square
        rand = randint( 0, len(empty_squares)-1 )

        return empty_squares[rand]

