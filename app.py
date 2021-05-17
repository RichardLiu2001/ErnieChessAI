########  imports  ##########
from flask import Flask, jsonify, request, render_template
from engine import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

    
 #########  run app  #########
app.run(debug=True)