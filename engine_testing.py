from engine import Engine

engine = Engine(0)

#print(engine.board.color_at)
#print(engine.get_legal_moves())
#engine.push_san('e4')
#print(engine.get_legal_moves())
best_move = [""]
print(engine.minimax(3, best_move))
print(best_move)