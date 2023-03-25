from typing import List, Tuple
        
class Automata:
    states: List[str]
    alphabets: List[str]
    transitions: List[Tuple[str, str, str]]

    def __init__(self, _transitions: List[Tuple[str, str, str]]):
        self.states = list(dict.fromkeys([x[0] for x in _transitions]))
        self.alphabets = self.states = list(dict.fromkeys([x[1] for x in _transitions]))
        self.transitions = _transitions
    
class Operations:
    first_automata: Automata
    second_automata: Automata
    
    def __init__(self, _first_automata: Automata, _second_automata: Automata) -> None:
        self.first_automata = _first_automata
        self.second_automata = _second_automata
    
    def direct_multiplication(self):
        return self.first_automata
