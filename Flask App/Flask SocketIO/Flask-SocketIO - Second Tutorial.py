# https://www.youtube.com/watch?v=zQDzNNt6xd4
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# Initialize Flask-SocketIO
socket = SocketIO(app)

@app.route('/')
def main():
    return render_template('main.html')

# Event Listener: when the server receives a message call, send back data
@socket.on('message') # message is one of the four predefined events
def handlemsg(msg):
    print(msg) # if client send data to this event bucket
    socket.send(msg) # sends the recieved message to the connected clients back to the message bucket
    emit('some-event', 'this is a custom event message') # emit lets us use custom named buckets. data will be sent to the custom bucket


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')

if __name__ == "__main__":
    socket.run(app)