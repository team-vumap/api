from functools import reduce
from operator import concat
from itertools import product

def flatten(lst):
    return reduce(concat, lst)

def cartesian_product(lst):
    return list(product(*lst))
