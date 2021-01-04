from random import randint

from .bot import Bot

class EasyBot(Bot):
    '''easy bot checks for must moves then plays randomly'''

    def Think(self, game):
        return self.random_move(game)