from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"richard" : {"age" : 19, "gender" : "male"},
        "tim" : {"age" : 69, "gender" : "?"}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data" : "posted"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__app__":
    app.run(debug=True)
