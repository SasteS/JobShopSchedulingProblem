from constants import *
import ParameterFns
import crossover
import mutation
import elitis
from Graphic_helper import average_value, raspored

def genetic(population_size, mutation_rate = 0.7, max_iter = 100, convergence_check = 0.005):
    CHROMOSOMES = generate_chromosome_list(population_size, JOBS, MACHINES, [])
    the_best_list = [] #najbolji hromozom
    avg_values = []
    list_of_averages_trough_time = []
    list_of_best_values_trough_time = []
    
    
    for i in range(max_iter):
        chromosome_dict, best_unit = ParameterFns.get_chromosome_rang_dict(CHROMOSOMES, JOBS, MACHINES)
        pairs = ParameterFns.rulette_selection(chromosome_dict)

        new_gen, old_gen = crossover.crossover(pairs)

        new_gen = mutation.mutation(new_gen, mutation_rate)
        CHROMOSOMES, the_best, values, the_best_value = elitis.elitis(new_gen, best_unit)
        CHROMOSOMES = generate_chromosome_list(population_size, JOBS, MACHINES, CHROMOSOMES)
        the_best_list.append(the_best)
        
        new_gen_avg = sum(values) / len(values)
        avg_values.append(new_gen_avg)
    
        #checks for convergence
        j = 0
        for k in range(len(avg_values) - 1):
            if abs(avg_values[k] - avg_values[k + 1]) <= convergence_check:
                j += 1
        if j > len(avg_values) / 2:
            return CHROMOSOMES, the_best, values

        list_of_averages_trough_time.append(average_value(values))
        list_of_best_values_trough_time.append(the_best_value)
        
        print("-"*50)
        print(i + 1)
        # print("Chromosomes = ")
        # for chromosome in CHROMOSOMES:
        #     print(chromosome)
        print()
        print("the_best = " + str(the_best))
        print()
        print("The best values's time: ", the_best_value)
        print()
        print("values = " + str(values))

    return CHROMOSOMES, the_best, values, list_of_averages_trough_time, list_of_best_values_trough_time