from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
# import json

import bingo_card_generator

# py -m venv venv
# venv\Scripts\activate

app = Flask(__name__)
Bootstrap(app)

# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

c_numbers = bingo_card_generator.bingo_call_numbers()


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/_next_number')
def next_number():

    n_ball = c_numbers[0]
    c_numbers.pop(0)
    return n_ball
    # return jsonify(result=n_ball)
    

@app.route('/')
def index(methods=['GET', 'POST']):
    
    b_numbers = bingo_card_generator.Bingo_card_generator()

    print(c_numbers[0])
    return render_template('index.html', bingo_numbers=b_numbers, next_ball=c_numbers)
    # return redirect(url_for('about'))


@app.route('/sessions')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):

    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('get ball')
def get_ball_event(json, methods=['GET', 'POST']):

    nb = next_number()
    print(nb)
    json['bingo'] = str(nb)
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('connect event')
def connect_event(json, methods=['GET', 'POST']):

    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    # app.run(debug=True)     # port=5001
    socketio.run(app, debug=True)


