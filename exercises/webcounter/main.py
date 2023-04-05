from flask import Flask, render_template

app = Flask('Web Counter')
# TODO: Use a database implementation instead of a dictionary so the data is saved persistent
database = {
    'number': 0
}


@app.route('/')
def home():
    return render_template('index.html', database=database)


@app.route('/increment')
def increment():
    database['number'] += 1
    print(database['number'])
    return render_template('index.html', database=database)


@app.route('/decrement')
def decrement():
    database['number'] -= 1
    print(database['number'])
    return render_template('index.html', database=database)


app.run('0.0.0.0', 81)
