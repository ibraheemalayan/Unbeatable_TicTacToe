from signs import X, O
from Game import Game
from bots.cli_player import CliPlayer
from signs import X, O

p1 = CliPlayer(X)
p2 = CliPlayer(O)

game = Game(p1, p2)

game.start()