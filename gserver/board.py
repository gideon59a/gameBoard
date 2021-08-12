import sys
sys.path.append('../') #this has been added so can be found in cmd window

class YYBoard():
    ''' Game borad actions. This parent class assumes:
    - two players
    - ...
    '''
    def __init__(self):
        self.player = "A"  # init the first player
        self.winner = ""  # equals to A, B, Tie, or null
