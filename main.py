from constants import *
import ParameterFns
import crossover

chromosome_dict = ParameterFns.get_chromosome_rang_dict(CHROMOSOMES, JOBS, MACHINES)
pairs = ParameterFns.rulette_selection(chromosome_dict)

d, r = crossover.crossover(pairs)

print("deca = " + str(d))
print("roditelji = " + str(r))