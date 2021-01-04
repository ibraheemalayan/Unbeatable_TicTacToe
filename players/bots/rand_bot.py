from .bot import Bot
from random import randint

class Rand_Bot(Bot):
    ''' stupid bot that plays randomly '''

    # overrides the default behaviour of checking for "must moves"
    # because this bot should be completely random
    def play(self, game):
        return self.think(game)

    # overrides the super method
    def think(self, game):

        return self.random_move(game)

