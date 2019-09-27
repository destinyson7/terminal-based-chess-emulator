from piece import Piece

class Knight(Piece):

    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.piece_type = 'knight'
        self.color = color
    
    def valid(self, initial, final, capture):
        letter1 = ord(initial[0])
        letter2 = ord(final[0])

        number1 = int(initial[1])
        number2 = int(final[1])
        
        if (abs(letter1 - letter2) == 2 and abs(number1 - number2) == 1 or (abs(number1 - number2) == 2 and abs(letter1 - letter2) == 1)):
            return True
        
        else:
            return False

    def move(self, initial, final, capture=False):
        try:
            assert(self.pos == initial)

        except:
            return False
        
        if self.valid(initial, final, capture):
            self.pos = final
            return True
        
        else:
            return False

    def disp(self):
        if self.color == 'Black':
            return ' Kb'
            
        else:
            return ' K '
        