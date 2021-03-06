from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    blue="Blue"
    return 'Hello True {0}!'.format(blue)

@app.route('/boo')
def hello_world():
    return 'BOO!'

@app.route('/boom')
def hello_world():
    return 'BOOM!'

@app.route('/zoom')
def hello_world():
    return 'ZOOM!'

@app.route('/doom')
def hello_world():
    return 'DOOM!'

@app.route('/room')
def hello_world():
    return 'ROOM!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 5000)))
