#!/usr/bin/env python
from threading import Lock, Thread, Event
from random import random
from time import sleep
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated random numbers to clients."""
    count = 0
    while True:
        number = round(random()*10, 3)
        print(number)
        #socketio.emit('newnumber', {'number': number}, namespace='/test')
        socketio.emit('server_response',
                      {'data': 'Server generated random number', 'number': number},
                      namespace='/test')
        socketio.sleep(1)    


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('server_response', {'data': 'Connected', 'number': 0})

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    #session['receive_count'] = session.get('receive_count', 0) + 1
    emit('server_response',
         {'data': 'Disconnected! Please refresh the page to reconnect!', 'number': 100})
    disconnect()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app)
