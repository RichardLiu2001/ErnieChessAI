########  imports  ##########
from flask import Flask, jsonify, request, render_template
#from engine import *
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers


if __name__ == '__main__':
    app.run(debug=True)