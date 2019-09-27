from piece import Piece
class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            temp = []
            for j in range(8):
                temp.append(Piece('a1', 'abc'))
            self.board.append(list(temp))

    def disp(self):
        check = 1
        strf = '   '
        for row in self.board:
            for i in range(2):
                for obj in row:
                    if i%2 == 0: # Print Board Scaffolding
                        strf += '+---'
                    else: # Print objects
                        strf += '|'
                        strf += obj.disp()
                if i%2 == 0:
                    strf += '+'
                else:
                    strf += '|'
                strf += '\n'

                if i%2 == 0:
                    strf += " " + str(9-check) + " "
                
                else:
                    strf += "   "
            check += 1
        for obj in self.board[-1]:
            strf += '+---'
        strf += '+'

        strf+= "\n     a   b   c   d   e   f   g   h "
        print(strf)
    
    # def update_board(self, inital, final):
        
    def chess_to_matrix_translator(self, pos):
        letter = pos[0]
        number = pos[1]
        letter_mapping = {'a': 0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g': 6, 'h': 7}
        row = int(8-int(number))
        col = int(letter_mapping[letter])
        return row, col

    def place(self, obj):
        row, col = self.chess_to_matrix_translator(obj.pos)
        self.board[row][col] = obj
        return









