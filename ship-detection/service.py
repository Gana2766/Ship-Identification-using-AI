from imageclassifier import img
from flask import Flask, request,send_file , make_response
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api
# from flask_cors import CORS

# import database as db


app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

# @app.route("/api/v1/users")
# def list_users():
#   return "user example"


app = Flask(__name__)
api = Api(app)

print(dir(api))

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        print("Got Detect Request")
        print(request.files['file1'])
        request.files['file1'].save('input.jpg')
        op='output.png'
        image_binary = img('input.jpg')
        # response = make_response(image_binary)
        # response.headers.set('Content-Type', 'image/jpeg')
        # response.headers.set('Content-Disposition', 'inline', filename=op)
        # return response
        # return send_file(op, mimetype='image/gif')
        return send_file('output.png')
        
api.add_resource(HelloWorld, '/detect')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
