var board = null
var game = new Chess()
var $status = $('#status')

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
  //window.alert(game.moves())

  var randomIdx = Math.floor(Math.random() * possibleMoves.length)
  move = possibleMoves[randomIdx]
  console.log("random move: " + move)
  //sendUserInfo(move)

  game.move(move)
  board.position(game.fen())
  updateStatus()
  
}

function makeComputerMove(move) {
  console.log("make computer move: " + move);
  game.move(move)
  board.position(game.fen())
  updateStatus()
  //return makeRandomMove();
}

    
function send_player_move(move) {

  $.ajax({
    type: "POST",
    url: "/_get_data/",
    data:JSON.stringify(move),
    contentType: 'application/json',
    dataType: "json",
    success: function(resp) {
      console.log("resp: " + resp);
      makeComputerMove(resp);
    }
  });
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

  console.log("player move: " + move.san)
  send_player_move(move.san);
  // make random legal move for black
  window.setTimeout(makeComputerMove, 250)
}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
  board.position(game.fen())
  updateStatus()
}

function updateStatus () {
  var status = ''

  var moveColor = 'White'
  if (game.turn() === 'b') {
    moveColor = 'Black'
  }

  // checkmate?
  if (game.in_checkmate()) {
    status = 'Game over, ' + moveColor + ' is in checkmate.'
  }

  // draw?
  else if (game.in_draw()) {
    status = 'Game over, drawn position'
  }

  // game still on
  else {
    status = moveColor + ' to move'

    // check?
    if (game.in_check()) {
      status += ', ' + moveColor + ' is in check'
    }
  }

  $status.html(status)
}

var config = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
}
board = Chessboard('board1', config)


updateStatus()