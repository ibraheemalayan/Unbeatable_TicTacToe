from random import randint

from .bot import Bot

class EasyBot(Bot):
    '''easy bot checks for must moves then plays randomly'''

    def Think(self, game):
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
