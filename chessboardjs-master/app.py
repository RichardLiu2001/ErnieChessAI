from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):

    userInfo = json.loads(userInfo)

    print('USER INFO RECEIVED')


if __name__ == '__main__':
    app.run(debug=True)   