from enums import Enums
from Game import Game
from players.cli_player import CliPlayer
from players.bots.rand_bot import Rand_Bot
from players.bots.easy_bot import EasyBot

enums = Enums()

p1 = CliPlayer(enums.X)
p2 = EasyBot(enums.O)

game = Game(p1, p2, enums)

game.start()
