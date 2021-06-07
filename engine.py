import chess
import enum
import random

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

    # gets the best move from the engine
    def get_move(self):
        best_move = None
        best_move_score = -1
        
        # shuffle move list so that it doesn't go back and forth
        #print(type(self.board.legal_moves.))
        #legal_moves = random.shuffle(self.board.legal_moves)

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

    def get_outcome(self):
        return self.board.outcome()

    def get_legal_moves(self):
        return self.board.legal_moves

    def push(self, move):
        return self.board.push(move)

#print(evaluate_position_fen(board.fen()))

# retrieves the chess.Move from user input
def get_player_move(engine):
    
    valid_move = False
    move = None

    while not valid_move:
        move_string = input("Enter your move: ")
        move = chess.Move.from_uci(move_string)
        #move = engine.board.parse_san(move_string)
        print(move)
        legal_moves = engine.get_legal_moves()
        is_valid = move in legal_moves

        if not is_valid:
            print("Not a legal move, ya fucken nerd\n")
        else:
            print("Legal move")
            valid_move = True
        
    return move


    


# plays a game against the engine
def play():
    color = input("enter your color: ")

    color_value = 0

    if color[0] == 'b' or color[0] == 'B':
        color_value = 1
    
    engine = Engine(color_value)
    #move = get_player_move(engine)
    #engine.push(move)
    #print(move)
    move = None
    player_turn = color_value == 0
    #print("engine outcome: " + str(engine.get_outcome()))
    while engine.get_outcome() == None:

        if player_turn:
            move = get_player_move(engine) 
            player_turn = False
        else:
            print("engine turn")
            player_turn = True
            move = engine.get_move()

        engine.push(move)
        print("move: " + str(move))
        print(engine.board)







    print("outcome: " + str(engine.get_outcome()))
    print(engine.board)

play()


#print(engine.get_move())