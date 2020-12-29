from enums import X, O
from Game import Game
from players.cli_player import CliPlayer
from players.bots.bot import Bot

p1 = Bot(X)
p2 = CliPlayer(O)

game = Game(p1, p2)

game.start()