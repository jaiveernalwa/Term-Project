from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['userInput']
    processed_text = user_input.upper()  # Example processing, just converting to uppercase
    return processed_text

if __name__ == '__main__':
    app.run(debug=True)
