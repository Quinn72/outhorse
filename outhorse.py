from flask import Flask, render_template, request, jsonify
import random
import string
import time

app = Flask(__name__)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

@app.route('/')
def index():
    return render_template('index.html', wait_time=0, random_str="", length=0)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        if length < 0:
            raise ValueError("Length must be a non-negative integer.")
    except ValueError as e:
        return jsonify(error=f"Error: {e}")

    wait_time = 2  # Set the wait time in seconds

    # Display the inputted amount and wait time in the console
    print(f"Inputted amount: {length}, Wait time: {wait_time} seconds")

    # Simulate a delay
    time.sleep(wait_time)

    random_str = generate_random_string(length)

    return jsonify(result={'random_str': random_str, 'length': length, 'wait_time': wait_time})

if __name__ == '__main__':
    app.run(debug=True)
