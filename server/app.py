from flask import Flask, make_response, jsonify, request


app = Flask(__name__)

@app.route('/') 
def application():
    return '<button>Welcome to my page!</button>', 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)