class Options:
    def __init__(self, opt):
        self.opt = opt
        if opt == 'paper':
            self.enemy= 'scissor'
        elif opt == 'scissor':
            self.enemy= 'rock'
        else:
            self.enemy = 'paper'
