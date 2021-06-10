from flask import request, Flask, render_template, jsonify,json

import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_get_data/', methods=['POST'])
def _get_data():
        data = {}
        data['move'] = request.json['move']       
        print(data, file=sys.stderr)
        nextMove = 'wrong move'
        return jsonify(nextMove)


if __name__ == "__main__":
    app.run(debug=True)