from enums import Enums
from Game import Game
from players.cli_player import CliPlayer
from players.bots.rand_bot import Rand_Bot
from players.bots.easy_bot import EasyBot
from players.bots.legend import XLegendBot

enums = Enums()

p1 = XLegendBot(enums.X)
p2 = CliPlayer(enums.O)

game = Game(p1, p2, enums)

game.start()
