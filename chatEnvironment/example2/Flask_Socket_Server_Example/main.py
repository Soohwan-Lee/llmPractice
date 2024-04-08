# original source: https://github.com/luvris2/python-example/tree/main?tab=readme-ov-file
# https://luvris2.tistory.com/851

from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__, template_folder=os.getcwd()+'/templates/')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    # socketio.run(app, host='192.168.0.78', port=4000, debug=True)