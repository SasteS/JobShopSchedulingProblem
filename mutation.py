import random
from constants import *

def mutation(chromosomes, mutation_rate):
    """
    parametri funkcije su:
    chromosomes - lista svih hromozoma u trenutnoj generaciji
    mutation_rate - broj koji oznacava stopu mutacije

    mutacija se vrsi tako sto se u drugom delu hromozoma zameni redosled 2 nasumicno odabrane masine

    potrebno je proveriti samo da li je novonastali redosled masina moguc,
    ukoliko nije, dodeljuje se random masina koja moze da izvrsava odredjenu operaciju
    """

    mutated_chromosomes = []
    for chromosome in chromosomes:
        mutated = []
        operations = chromosome[0]
        machines = chromosome[1]
        if random.random() < mutation_rate:
            pos1 = random.randrange(0, len(machines))
            pos2 = random.randrange(0, len(machines))

            machines[pos1], machines[pos2] = machines[pos2], machines[pos1]

            #prolazimo kroz masine i kroz poslove da vidimo da li je novi redosled masina dobar
            for j in range(len(JOBS_KEYS)):
                o = 0
                for i in range(len(machines)):
                    job = operations[i]
                    machine = machines[i]

                    if job == JOBS_KEYS[j]:
                        proces_duration = MACHINES[machine][job][o]
                        if MACHINES[machine][job][o] == 0:
                            #ukoliko je 0 onda mora da pronadje masinu koja radi
                            while proces_duration != 0:
                                new_m = random.choice(MACHINES.keys())
                                proces_duration = MACHINES[machine][job][o]
                                machines[i] = new_m
            
        mutated.append(operations)
        mutated.append(machines)
        mutated_chromosomes.append(mutated)
                            
    return mutated_chromosomes