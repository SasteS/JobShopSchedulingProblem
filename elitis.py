from fitness_function import fitness_function
from constants import *

def elitis(children, best_parent):
    values = []
    dictionary = {}
    for i in range(len(children)):
        value = fitness_function(children[i], MACHINES, JOBS_KEYS, True)
        values.append(value)
        dictionary[value] = children[i]


    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}

    best = best_parent.chromosome

    worst_child = list(sorted_dict.values())[-1]
    worst_child_value = list(sorted_dict.keys())[-1]
    best_child = list(sorted_dict.values())[0]
    best_child_value = list(sorted_dict.keys())[0]

    children.remove(worst_child)
    children.append(best)

    value_of_parent = fitness_function(best, MACHINES, JOBS_KEYS, True)

    the_best_value = 0
    values.remove(worst_child_value)
    if value_of_parent > best_child_value:
        the_best = best_child
        values.append(best_child_value)
        the_best_value = best_child_value
    else:
        the_best = best
        values.append(value_of_parent)
        the_best_value = value_of_parent
    
    return children, the_best, values, the_best_value