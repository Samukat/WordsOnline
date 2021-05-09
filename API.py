from flask import Flask, request, render_template, make_response, url_for, flash
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import flask_jsonpify

host = "192.168.0.138"
port = 3306

db_connect = create_engine("")
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
api = Api(app)

class Nothing(Resource):
    def get(self):
        #return flask_jsonpify.jsonpify({'message':'Welcome to the words online API'})
        #return render_template('index.html', mimetype='html')
        headers = {'Content-Type': 'text/html', 'api':"123"}
        return make_response(render_template('index.html'),200,headers)
    def post(self):
        headers = {'Content-Type': 'text/html'}
        print(request.form["ch"])
        
        conn = db_connect.connect()
        query = conn.execute("select * from wordsonline where channel = '{}'".format(request.form["ch"]))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        #return make_response(render_template('index.html', data="Wow so empty"),200,headers)

        
        if len(list(query)) == 0:
            return make_response(render_template('index.html', data="Wow so empty"),200,headers)
        elif result['data'][0]['pass'] == None:
            return make_response(render_template('index.html', data=result['data'][0]['words']),200,headers)


        
        
        
    
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from wordsonline") # This line performs query and returns json result
        return {'Word_IDs': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID


class Words_Channel_CLOSED(Resource):
    def get(self, channel, password):
        conn = db_connect.connect()
        query = conn.execute("select * from wordsonline where channel = '{}'".format(channel))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

        if len(list(query)) == 0:
            return (flask_jsonpify.jsonpify({'message':'Channel name does not exist'}))
        if result['data'][0]['pass'] != password:
            return (flask_jsonpify.jsonpify({'message':'Invalid Password'}))

        return flask_jsonpify.jsonpify(result)


class Words_Channel_OPEN(Resource):
    def get(self, channel):
        conn = db_connect.connect()
        query = conn.execute("select * from wordsonline where channel = '{}'".format(channel))

        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

        if len(list(query)) == 0:
            return (flask_jsonpify.jsonpify({'message':'Channel name does not exist'}))
        if result['data'][0]['pass'] != None:
            return (flask_jsonpify.jsonpify({'message':'Invalid Password'}))

        return(flask_jsonpify.jsonpify(result))


class Ping_Test(Resource):
    def get(self):
        pass

api.add_resource(Nothing, '/', methods=["POST","GET"]) # Route_1
api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Ping_Test, '/ping')
api.add_resource(Words_Channel_OPEN, '/Words_Channel/<channel>')
api.add_resource(Words_Channel_CLOSED, '/Words_Channel/<channel>/<password>')



if __name__ == '__main__':
     app.run(host=host, port=port)
