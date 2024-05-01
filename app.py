from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy questions and answers
questions = ["What is the capital of France?", "What is the largest mammal?", "What is 2 + 2?"]
answers = ["paris", "blue whale", "4"]

score = 0
lives = 3
current_question_index = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global score, lives, current_question_index
    user_answer = request.form['answer'].lower()
    correct_answer = answers[current_question_index]

    if user_answer == correct_answer:
        score += 1
    else:
        lives -= 1

    current_question_index += 1
    if current_question_index >= len(questions):
        # Game over
        return "Game Over! Final Score: {} Lives: {}".format(score, lives)

    return render_template('index.html', question=questions[current_question_index], score=score, lives=lives)

if __name__ == '__main__':
    app.run(debug=True)
