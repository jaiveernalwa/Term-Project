# game_app.py
from flask import Flask, render_template, request
from game import Game, Player

app = Flask(__name__)
game = Game()
player = Player()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        choice = int(request.form['choice']) - 1
        action = game.get_current_actions()[choice]
        game.handle_action(action, player)
    return render_template('game.html', scene=game.current_scene, actions=game.get_current_actions())

if __name__ == '__main__':
    app.run(debug=True)
