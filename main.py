from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__) 


@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>route 1 test</h1>"




@app.route('/test')
def info():
    return "<h1>route 2 test</h1>"



api = Api(app)



class HelloWorld(Resource):


    def get(self):
        return {'hello':'world'}



api.add_resource(HelloWorld(), '/')



if __name__ == '__main__' :
    app.run()


