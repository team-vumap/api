from flask import Flask
from models.automata import Automata, Operations
from typing import List, Tuple
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Test route to see if the API calls work
    """
    return { 'data': 'Hello world' }

@app.route('/automata',  options=["POST"])
def get_all_init_automata():
    """
    """
    return json.dumps(Automata().__dict__)

@app.route('/automata/multiply', options=["POST"])
def direct_multiply_automata(first_automata: List[Tuple[str, str, str]], second_automata: List[Tuple[str, str, str]]):
    """
    """
    operation = Operations(Automata(first_automata), Automata(second_automata))
    result = operation.direct_multiplication()
    return json.dumps(result.__dict__)
