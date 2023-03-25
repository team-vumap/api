from typing import List, Tuple
from functools import reduce
from operator import concat
from itertools import product

def flatten(lst: List[List[str]]) -> List[str]:
    return reduce(concat, lst)

def cartesian_product(lst: List[List[str]]) -> List[List[str]]:
    return list(product(*lst))
