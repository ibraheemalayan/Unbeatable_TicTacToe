from bots.player import XOPlayer
from signs import get_sign, get_state, X, O

class CliPlayer(XOPlayer):
    ''' CLI XO Player object '''

    def __init__(self, sign):
        super().__init__(sign)

    def play(self, game):

        print(game.get_printable_grid())

        num = input("> " + get_sign(self.sign) + "'s turn, enter square number: ")

        if not self.valid_input(num, game):
            return self.play(game)

        return int(num) - 1
    
    def valid_input(self, raw, game):

        if not raw.isnumeric():
            print("> invalid input, should be a number !")
            return False

        num = int(raw) - 1

        if num not in range(0,9):
            print("> invalid input, should be within 1-9 !")
            return False

        if game.square_full(num):
            print("> invalid input, should be an empty square not full !")
            return False

        return True

    def done(self, game):

        print(game.get_printable_grid())

        state = game.game_state()

        str_state = get_state(state)

        print(" Final state: " + str_state )
