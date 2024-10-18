import numpy as np
import math

def F1(solution):
    return sum(x**2 for x in solution)

def F2(solution):
    return sum(math.sin(x) for x in solution)

def get_info(function_name):
    if function_name == 'F1':
        return [F1, -100, 100, 2]
    if function_name == 'F2':
        return [F2, -100, 100, 2]        