import chess
import enum

board = chess.Board()

# white = 0, black = 1
turn = 0

#print(board.legal_moves)
#print(board.color_at)

#print(vars(board))
print(board.piece_map)

piece_values = {
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


# returns the sum of all pieces on the board from fen
def evaluate_position_fen(fen):

    white_sum = 0
    black_sum = 0

    piece_fen = fen.split()[0]

    for piece in piece_fen:
        value = piece_values[piece]
        if piece.isupper():
            white_sum += value
        else:
            black_sum += value

    return white_sum, black_sum

def get_move():
    best_move = None
    best_move_score = -1

    for move in board.legal_moves:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return move
        current_move_score = evaluate_position_fen(board.fen())[turn]

        if current_move_score > best_move_score:
            best_move_score = current_move_score
            best_move = move

        board.pop()

    return best_move


