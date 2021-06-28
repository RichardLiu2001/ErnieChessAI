from engine import Engine

engine = Engine(0)

#print(engine.board.color_at)
#print(engine.get_legal_moves())
#engine.push_san('e4')
#print(engine.get_legal_moves())
best_move = [""]
print(engine.board.turn)
print(engine.board.turn)
print(engine.minimax(1, best_move))
print(best_move)