from random import randint

from .plans import generate_plans
from .bot import Bot

class XLegendBot(Bot):
    '''easy bot checks for must moves then plays randomly'''

    def __init__(self, sign):
        super().__init__(sign)
        self.plans = generate_plans()
        self.on_plan = False
        self.plan = []

    def Think(self, game):

        if self.step(game) == 0:
            print("BOT: playing first step")
            return self.first_step(game)

        
        if self.on_plan:
            print("BOT: playing onplan")
            return self.play_plan(game)

        self.maintaine_plan(game)

        print("BOT: playing maintained plan")

        return self.play_plan(game) if self.on_plan else self.random_move(game)

    def play_plan(self, game):

        step_num = len(game.gameplay)

        return self.plan[step_num]
    
    def maintaine_plan(self, game):

        print("BOT: maintaining plan")

        self.plan = game.gameplay.copy()

        if self.step(game) == 2:

            if game.gameplay[1] == 4:
                next_move = self.plans['opposite_corner_of'][game.gameplay[0]]
                self.on_plan = True
                self.plan.append(next_move)

        

    def tactics(self):

        return {
            'corner':{
                'center':{
                    [
                        'opposite_corner'
                    ]
                }
            }
        }


    def step(self, game):
        return len(game.gameplay)


    # Plays the first step
    def first_step(self, game):
        
        # chooses a random corner

        rand = randint(0,3)

        return self.plans['corners'][rand]
    
    def get_remaining_corners(self, game):

        remaining_corners = []

        for s in self.plans['corners']:
            if not game.square_full(s):
                remaining_corners.append(s)
        
        return remaining_corners

    def get_near_edges(self, game, corner):
        return self.plans['near_edges'][corner]

    def get_far_edges(self, game, corner):
        return self.plans['far_edges'][corner]

    def is_near(self, a, b):

        sub = a-b if (a > b) else b-a
            
        if sub == 1 or sub == 3:
            return True
        
        return False
