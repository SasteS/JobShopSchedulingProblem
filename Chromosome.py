import random
#import ParameterFns

class Chromosome():
    def __init__(self, jobs, machines, chromosome):
        if len(chromosome) == 0:
            self.chromosome = generate_chromosome(jobs, machines)
        else:
            self.chromosome = chromosome

    def __str__(self):
        return "iz klase : " + str(self.chromosome)

def generate_chromosome(jobs_dict, machines_dict):
    """
    example:
        jobs_dict = {"J1" : [p1, p2, p3], "J2" : [p1, p2]}
        machines_dict = [M1, M2, M3]

        len(jobs_dict[J1]) = 3
        len(jobs_dict[J2]) = 2

        chromosome: [["J1", "J2", "J2", "J1", "J2"]
                    [M1, M1, M3, M2, M1]]
    """
    job_slot = [] #lista procesa; na mestu procesa stoji kljuc od posla ciji je proces
    machine_slot = [] #lista masina koje obradjuju proces iz job_slot-a na istoj poziciji
    
    all_jobs_occurance_counter = {} #bice potreban pri punjenju job_slot gena
    for job_key in jobs_dict.keys(): #lista kljuceva "J1", "J2", ...
        all_jobs_occurance_counter.update({job_key : 0})
    
    #puni job_slot kljucevima "J1", "J2", ...
    while True:
        choice = random.choice(list(jobs_dict.keys()))
        if all_jobs_occurance_counter[choice] < jobs_dict[choice]:
            all_jobs_occurance_counter[choice] += 1
            job_slot.append(choice)

            #ovaj deo sluzi da spreci da broj procesa jednog posla prekoraci broj iz prosledjenog dictionary-ja
            all_same = True
            for job in jobs_dict:
                if all_jobs_occurance_counter[job] != jobs_dict[job]:
                    all_same = False
                    break
            if all_same:
                break


    for job_key in jobs_dict.keys(): #resetuje za masine sada
        all_jobs_occurance_counter[job_key] = 0

    #puni machine_slot kljucevima "M1", "M2", ...
    for job_key in job_slot:
        while True:
            choice = random.choice(list(machines_dict.keys()))
            temp_machine = machines_dict[choice]
            #proveri da li masina moze da izvrsava operaciju na poziciji posla iz job_slota
            if list(temp_machine[job_key])[all_jobs_occurance_counter[job_key]] != 0:   
                machine_slot.append(choice)
                #koristi se da bi pratio pozicije operacija tipa ako je job_slot = ['J2', 'J1', 'J2', 'J1', 'J1'] i job_key = 'J1' na indexu 1 u all_jobs_occurance_counter[job_key] on sada pamti da je prva operacija predjena
                all_jobs_occurance_counter[job_key] += 1
                break

    chromosome = [job_slot, machine_slot]
    #print("chromosome = " + str(chromosome))
    return chromosome

#p = {"J1" : 3, "J2" : 2}
#m = {"M1" : { "J1" : [2, 5, 2] , "J2" : [10, 2] }, "M2" : { "J1" : [2, 0, 5] , "J2" : [10, 2] }, "M3" : { "J1" : [0, 5, 0] , "J2" : [10, 0] }}

# p = ParameterFns.Generate_Jobs(2, 3)
# m = ParameterFns.Generate_Machines(3, p, 10)

# print(p)
# print(m)

# generate_chromosome(p, m)