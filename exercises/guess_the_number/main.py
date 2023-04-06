"""
This is a Flask web app demonstrating the following concepts:
String Interpolation
Functions
Random
Dictionaries

And the Web Development concepts of:
Routing
GET Requests
POST Requests
"""
from random import choice
from flask import Flask, render_template, request

db = {'history': [],
      'computer_number': choice(range(1, 101))}


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def show_index():
    if request.method == 'POST':
        guess = int(request.form['number_guess'])
        message = check_number_show_msg(guessed_num=guess, computed_num=db['computer_number'])
        db['history'].append(message)
    return render_template('index.html', guesses=reversed(db['history']))


@app.route('/reset')
def show_reset():
    db['history'].clear()
    db['computer_number'] = choice(range(1, 101))
    return render_template('index.html', guesses=db['history'])


def check_number_show_msg(guessed_num: int, computed_num: int) -> str:
    """
    This function checks the guess and returns the hint message

    >>> check_number_show_msg(5, 50)
    '5 is too low ⏫'

    >>> check_number_show_msg(75, 50)
    '75 is too high ⏬'

    >>> check_number_show_msg(50, 50)
    '50 is correct ✔'

    :param guessed_num: Number the user guesses
    :param computed_num: Actual number picked by the computer
    :return: String of the outcome
    """
    if guessed_num < computed_num:
        return f"{guessed_num} is too low ⏫"
    elif guessed_num > computed_num:
        return f"{guessed_num} is too high ⏬"
    else:
        return f"{guessed_num} is correct ✔"


app.run("0.0.0.0", 81)
