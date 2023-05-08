# https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/
# Flask demo to test the operation of flask with socket.it. Web page constantly update with random numbers from a background Py process

from argparse import Namespace
from asyncio.log import logger
from threading import Thread
from flask import Flask, render_template # import class
from flask_socketio import SocketIO, emit
from random import random
from time import sleep
from threading import Thread, Event

app = Flask(__name__, template_folder='templates') # set instance to flask, so flask knows where to look for 
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

# Random number generator thread
thread = Thread()
thread_stop_event = Event()


@socketio.on('my event') # Decorator to catch an event called 'my event'
def test_message(message): # test_message() is the event vallback function.
    emit('my response', {'data':'got it!'}) # Trigger a new event called 'my response' that can be caught by another callback later in the program

if __name__ == '__main__':
    socketio.run(app)

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        # Generate a rand num every 1 sec and emit to a socketio instance (broadcast)
        # infinit loop of magical random numbers
        print('Making random numbers')

        while not thread_stop_event.isSet():
            number = round(random()*10,3)
            print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()

# Start Asynch num gen
@app.route('/')
def index():
    # only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    # Start the random number generator thread only if the thread has notbeen started before.
    if not thread.is_alive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()