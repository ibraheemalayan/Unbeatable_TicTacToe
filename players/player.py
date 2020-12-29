class XOPlayer:
    ''' 
    this class represnts the xobot, it has the basic functions for a bot to play tic tac toe 
    Available functions are :
        
        NextStep()    
            should be overridden according to difficultiy level

        Grid object

    '''
    def __init__(self, sign):
        ''' Construct an XOBot object'''
        self.sign = sign

    def play(self, game):
        ''' This method is abstract (should be overridden) '''
        pass

    def done(self, state):
        ''' This method is abstract (should be overridden) and is intended for cli players'''
        pass
