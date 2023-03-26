from flask import Flask, request
from flask_cors import CORS
from models.automata import Automata, Operations
import json

app = Flask(__name__)
CORS(app)

known_automta = {
    'E.Coli': [[0,1,1],[1,1,2],[2,1,0],[1,0,0],[2,0,1],[0,0,2]]
}

@app.route('/')
def hello_world():
    """
    Test route to see if the API calls work
    """
    return { 'data': 'Hello world' }

@app.route('/automata', methods=["GET"])
def get_all_init_automata():
    """
    Get all of the initial automata (we need to create these)
    """
    return json.dumps(list(known_automta.keys()))

@app.route('/automata/name',  methods=["POST"])
def get_named_automata():
    """
    Get the transition for that particular bacteria
    """
    print(request.args)
    name = request.args.get("name")
    transition = known_automta[name]
    return json.dumps(Automata(name, transition).__dict__)

@app.route('/automata/multiply', methods=["POST"])
def direct_multiply_automata():
    """
    Direct multiply two automata
    """
    json_data = request.get_json()
    first_automata = json_data['first_automata']['transitions']
    first_automata_name = json_data['first_automata']['name']
    second_automata = json_data['second_automata']['transitions']
    second_automata_name = json_data['second_automata']['name']
    operation = Operations(Automata(first_automata_name, first_automata), Automata(second_automata_name, second_automata))
    result = operation.direct_multiplication()
    known_automta[result.name] = result.transitions;
    return json.dumps(result.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
