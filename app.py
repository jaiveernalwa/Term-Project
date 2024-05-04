from flask import Flask, render_template, request, redirect, url_for
from trivia import trivia_game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    name = request.form['name']
    trivia_game()
    return redirect(url_for('play_game', name=name))

@app.route('/play/<name>')
def play_game(name):
    return render_template('play.html', name=name, score=0, lives=3, question="")

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    # Can't process answer
    return redirect(url_for('play_game'))

if __name__ == '__main__':
    app.run(debug=True)
