from enums import X, O
from Game import Game
from players.cli_player import CliPlayer
from players.bots.rand_bot import Rand_Bot

p1 = Rand_Bot(X)
p2 = CliPlayer(O)

game = Game(p1, p2)

game.start()