from piece import Piece

class King(Piece):

    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.piece_type = 'king'
        self.color = color

    def valid(self, initial, final, capture):
        letter1 = ord(initial[0])
        letter2 = ord(final[0])

        number1 = int(initial[1])
        number2 = int(final[1])

        if((abs(number1 - number2) == 1 and (abs(letter1 - letter2) == 0 or abs(letter1 - letter2) == 1)) or (abs(letter1 - letter2) == 1 and (abs(number1 - number2) == 0 or abs(number1 - number2) == 1))):
            return True
        
        else:
            return False

    def move(self, initial, final, capture):
        try:
            assert(self.pos == initial)
        
        except:
            return False
        
        if self.valid(initial, final, capture=False):
            self.pos = final
            return True
        
        else:
            return False
        
    
    def disp(self):
        if self.color == 'Black':
            return  '<b>'
        
        else:
            return '<w>'
