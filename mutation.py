import random


MACHINES = {
    "M1" : {"J1" : [5, 7], "J2" : [4, 2]},
    "M2" : {"J1" : [1, 3], "J2" : [6, 8]},
    "M3" : {"J1" : [9, 0], "J2" : [11, 12]}
}

JOBS = ["J1", "J2"]

CHROMOSOMES = [[["J2","J1","J1","J2"],["M2","M3","M2","M1"]], 
                [["J1","J2","J1","J2"],["M1","M3","M2","M3"]],
                [["J2","J2","J1","J1"],["M2","M3","M2","M1"]], 
                [["J1","J2","J2","J1"],["M3","M3","M1","M1"]]]



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
            for j in range(len(JOBS)):
                o = 0
                for i in range(len(machines)):
                    job = operations[i]
                    machine = machines[i]

                    if job == JOBS[j]:
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

if __name__ == "__main__":
    novi = mutation(CHROMOSOMES, 0.2)
    for n in novi:
        print(n)