from flask import request, Flask, render_template, jsonify, json, send_file

import sys

app = Flask(__name__)

@app.route('/')
def index():
    print("index")
    return render_template('index.html')


@app.route('/_get_data/', methods=['POST'])
def _get_data():
        print("incoming data: " + str(request.json))
        
        #data = {}
        #data['move'] = request.json['move']       
        #print(data, file=sys.stderr)
        nextMove = 'wrong move'
        return jsonify(nextMove)

@app.route('/img/chesspieces/wikipedia/wB.png')
def get_wB():
      return send_file('img/chesspieces/wikipedia/wB.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/wK.png')
def get_wK():
      return send_file('img/chesspieces/wikipedia/wK.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/wN.png')
def get_wN():
      return send_file('img/chesspieces/wikipedia/wN.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/wP.png')
def get_wP():
      return send_file('img/chesspieces/wikipedia/wP.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/wQ.png')
def get_wQ():
      return send_file('img/chesspieces/wikipedia/wQ.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/wR.png')
def get_wR():
      return send_file('img/chesspieces/wikipedia/wR.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bB.png')
def get_bB():
      return send_file('img/chesspieces/wikipedia/bB.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bK.png')
def get_bK():
      return send_file('img/chesspieces/wikipedia/bK.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bN.png')
def get_bN():
      return send_file('img/chesspieces/wikipedia/bN.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bP.png')
def get_bP():
      return send_file('img/chesspieces/wikipedia/bP.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bQ.png')
def get_bQ():
      return send_file('img/chesspieces/wikipedia/bQ.png', mimetype='image/png')

@app.route('/img/chesspieces/wikipedia/bR.png')
def get_bR():
      return send_file('img/chesspieces/wikipedia/bR.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)