// NOTE: this example uses the chess.js library:
// https://github.com/jhlywa/chess.js
// import { Chess } from "./js/chess.js";
// NOTE: this example uses the chess.js library:
// https://github.com/jhlywa/chess.js

//const { Chess } = require('./node_modules/chess.js');
//const { Chessboard } = require('./js/chessboard-0.3.0.js'); 
var board = null
var game = new Chess()


function onDragStart (source, piece, position, orientation) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // only pick up pieces for White
  if (piece.search(/^b/) !== -1) return false
}

function makeRandomMove () {
  var possibleMoves = game.moves()

  // game over
  if (possibleMoves.length === 0) return

  var randomIdx = Math.floor(Math.random() * possibleMoves.length)
  game.move(possibleMoves[randomIdx])
  board.position(game.fen())
}

function onDrop (source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })

  // illegal move
  if (move === null) return 'snapback'

  // make random legal move for black
  window.setTimeout(makeRandomMove, 250)
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
  board.position(game.fen())
}
/*
var config = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
}
//board = Chessboard('board1', config)
*/

// from simple github tutorial

var config = {
  position: 'start',
  draggable: true
}

var board1 = ChessBoard('board1', config);


// random game
/*
const { Chess } = require('./node_modules/chess.js');
const chess = new Chess();

while (!chess.game_over()) {
    const moves = chess.moves()
    const move = moves[Math.floor(Math.random() * moves.length)]
    chess.move(move)
}
console.log(chess.pgn())
*/