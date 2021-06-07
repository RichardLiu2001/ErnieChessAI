from flask import Flask, request
app = Flask(__name__)

@app.route('/chess', methods=['POST'])

def get_names():
    move = "no move"
    if request.method == 'POST':
	    move = request.get_json()
    
    print("move: " + move)
        #print("MOVE: " + move)

if __name__ == "__app__":
    app.run(debug=True)