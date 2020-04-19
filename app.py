from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
# import json

import bingo_card_generator

# py -m venv venv
# venv\Scripts\activate

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

c_numbers = bingo_card_generator.bingo_call_numbers()
numbers_removed = []
# ball_val = 0

@app.route('/_next_number')
def next_number():

    n_ball = c_numbers[0]
    numbers_removed.insert(0,n_ball)
    c_numbers.pop(0)
    return n_ball
    # return jsonify(result=n_ball)
    

@app.route('/')
def index(methods=['GET', 'POST']):
    
    b_numbers = bingo_card_generator.Bingo_card_generator()

    print(c_numbers[0])
    return render_template('index.html', bingo_numbers=b_numbers) # , next_ball=c_numbers)
    # return redirect(url_for('about'))


@app.route('/index_admin')
def index_admin(methods=['GET', 'POST']):   
    b_numbers = bingo_card_generator.Bingo_card_generator()

    print(c_numbers[0])
    return render_template('index_admin.html', bingo_numbers=b_numbers) # , next_ball=c_numbers)



@app.route('/sessions')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):

    print('received my event event: ' + str(json))
    socketio.emit('my chat response', json, callback=messageReceived)


# def retain_ball_val(v_ball_val):
#     ball_val = v_ball_val
    

@socketio.on('get ball')
def get_ball_event(json, methods=['GET', 'POST']):

    nb = next_number()
    print(nb)
    with open('bingoball.txt', 'w') as fo:
        print(nb, file=fo)

    json['bingo'] = str(nb)
    ball_val = str(nb)
    
    print('received my event get ball: ' + str(json) + 'ball_val ' + ball_val)
    socketio.emit('my bingo response', json,  broadcast=True)
    # io.emit('my bingo response', json, callback=messageReceived)


@socketio.on('connect event')
def connect_event(json, methods=['GET', 'POST']):
    

    # with open('bingoball.txt', 'r') as fo:
    #     bingoo = fo
    #     print(bingoo)
    
    # f = open("bingoball.txt", "r")

    # print('wide ' + f.read())
    # p = f.read()

    # print(len(c_numbers))

    if len(numbers_removed) == 0:
        json['c_ball_val'] = '0'
    else:
        json['c_ball_val'] = numbers_removed[0]
    print('received my connect event: ' + str(json))
    socketio.emit('my connect response', json, broadcast=True) #callback=messageReceived,


@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    # app.run(debug=True)     # port=5001
    socketio.run(app) #, debug=True


