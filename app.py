from flask import Flask, render_template, jsonify
import json
import random
import os 

app = Flask(__name__)

# This function reads the data and returns a list of 5 random quotes
def get_random_quotes():
    """Reads quotes from file, shuffles, and returns a random selection."""
    file_path = os.path.join(app.root_path, 'api', 'quotes.json')
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            random.shuffle(data)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        
    return data[:5]

# Endpoint for the HTML web page
# This route returns a full HTML document
@app.route('/')
def home():
    quotes = get_random_quotes()
    return render_template('index.html', quotes=quotes)

# Endpoint for the JSON API
# This route returns a JSON array of the 5 random quotes
@app.route('/api/quotes')
def api_quotes():
    quotes = get_random_quotes()
    # The jsonify function serializes the Python list to a JSON response
    return jsonify(quotes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
