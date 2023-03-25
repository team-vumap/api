from operator import concat
from itertools import product

def cartesian_product(lst):
    return list(product(*lst))

class Automata:
    # states: List[str]
    # alphabets: List[str]
    # transitions: List[Tuple[str, str, str]]

    def __init__(self, _transitions):
        self.states = list(dict.fromkeys([x[0] for x in _transitions]))
        self.alphabets = list(dict.fromkeys([x[1] for x in _transitions]))
        self.transitions = _transitions
    
    def find_state(self, state, letter):
        return list(filter(lambda x: x[0] == state and x[1] == letter, self.transitions))[0][2]
    
    def transition(self, state, letter):
        return self.find_state(state, letter)
    
class Operations:
    first_automata: Automata
    second_automata: Automata
    
    def __init__(self, _first_automata: Automata, _second_automata: Automata) -> None:
        self.first_automata = _first_automata
        self.second_automata = _second_automata
    
    def direct_multiplication(self):
        result_states = cartesian_product([self.first_automata.states, self.second_automata.states])
        result_alphabets = cartesian_product([self.first_automata.alphabets, self.second_automata.alphabets])
        result_transitions = []
        for state in result_states:
            for letter in result_alphabets:
                transition_state_first = self.first_automata.transition(state[0], letter[0])
                transition_state_second = self.second_automata.transition(state[1], letter[1])
                transition_state = (transition_state_first, transition_state_second)
                result_transitions.append((state, letter, transition_state))
        
        return Automata(result_transitions)
