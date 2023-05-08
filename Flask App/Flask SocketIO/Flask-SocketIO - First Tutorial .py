# https://www.youtube.com/watch?v=MV23luBeunI
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socket = SocketIO(app)

fruit_list = ['apple', 'pear', 'banana', 'mango']
i = 0

@app.route('/')
def main():
    return render_template('main.html')

# Event Listener: when the server receives a message call, send back data
@socket.on('message')
def handlemsg(msg):
    print(msg)
    global i
    if i < len(fruit_list):
        socket.send(fruit_list[i])
        i +=1


if __name__ == "__main__":
    socket.run(app)