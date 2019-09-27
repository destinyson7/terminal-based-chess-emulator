from piece import Piece

class Pawn(Piece):
    # piece_type = 'pawn'

    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.piece_type = 'pawn'
        self.color = color

    def valid(self, initial, final, capture):
        letter1 = ord(initial[0])
        letter2 = ord(final[0])
        number1 = int(initial[1])
        number2 = int(final[1])
        if self.color == 'White':            
            if number1 == 2 and number2 == 4:
                if letter1 == letter2:
                    return True

            else:
                if capture:
                    if number2-number1 == 1 and abs(letter2-letter1) == 1 :
                        return True
                else:
                    if number2-number1 == 1 and abs(letter2-letter1) == 0:
                        return True
        else:
            if number1 == 7 and number2 == 5:
                if letter1 == letter2:
                    return True
            
            else:
                if capture:
                    if number2-number1 == -1 and abs(letter2-letter1) == 1 :
                        return True
                else:
                    if number2-number1 == -1 and abs(letter2-letter1) == 0:
                        return True
        return False

    def move(self, initial, final, capture=False):
        try:
            assert(self.pos == initial)
        except:
            return False
        if self.valid(initial, final, capture):
            self.pos = final
            return True
        

    def disp(self):
        if self.color == 'Black':
            return ' Pb'

        else:
            return ' P '

