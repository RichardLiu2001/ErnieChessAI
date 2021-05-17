import chess
import enum


class Engine:
# white = 0, black = 1
#turn = 0
    def __init__(self, engine_color):

        self.piece_values = {
            'r': 5,
            'R': 5,
            'b': 3,
            'B': 3,
            'N': 3,
            'n': 3,
            'P': 1,
            'p': 1,
            'Q': 9,
            'q': 9,
            'K': 0,
            'k': 0
        }

        self.engine_color = engine_color
        self.board = chess.Board()


    # returns the sum of all pieces on the board from fen
    def evaluate_position_fen(self):

        white_sum = 0
        black_sum = 0

        piece_fen = self.board.fen().split()[0]

        for piece in piece_fen:
            if piece in self.piece_values:
                value = self.piece_values[piece]
                if piece.isupper():
                    white_sum += value
                else:
                    black_sum += value

        return white_sum, black_sum


    def get_move(self):
        best_move = None
        best_move_score = -1

        for move in self.board.legal_moves:
            self.board.push(move)
            if self.board.is_checkmate():
                self.board.pop()
                return move
            current_move_score = self.evaluate_position_fen()[self.engine_color]

            if current_move_score > best_move_score:
                best_move_score = current_move_score
                best_move = move

            self.board.pop()

        return best_move


#print(evaluate_position_fen(board.fen()))

engine = Engine(0)

#print(engine.get_move())