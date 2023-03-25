from flask import Flask, request
from models.automata import Automata, Operations
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Test route to see if the API calls work
    """
    return { 'data': 'Hello world' }

@app.route('/automata',  methods=["POST"])
def get_all_init_automata():
    """
    Get all of the initial automata (we need to create these)
    """
    return json.dumps(Automata([]).__dict__)

@app.route('/automata/multiply', methods=["POST"])
def direct_multiply_automata():
    """
    Direct multiply two automata
    """
    json_data = request.get_json()
    first_automata = json_data['first_automata']
    second_automata = json_data['second_automata']
    operation = Operations(Automata(first_automata), Automata(second_automata))
    result = operation.direct_multiplication()
    return json.dumps(result.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
