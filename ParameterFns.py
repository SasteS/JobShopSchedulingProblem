import random
from Chromosome import *
from fitness_function import *

def generate_Jobs(num_of_jobs, num_of_operations):
    jobs = {}
    for i in range(num_of_jobs):
        job_key = "J" + str(i + 1)
        job = {job_key : random.randrange(2, num_of_operations + 1)}
        jobs.update(job)
    return jobs

def generate_Machines(num_of_machines, jobs, machine_times_max):
    """
    machine_times_max - uzima to kao maximalno vreme koje moze dati maisini,
    stavlja ga u random i ide od 0 do maxa
    """
    machines = {}
    for i in range(num_of_machines):
        machine_key = "M" + str(i + 1)

        machine_inner_dict = {}
        for key in jobs.keys():
            machine_times = []
        
            for i in range(jobs[key]):
                machine_times.append(random.randrange(0, machine_times_max))

            machine_inner_dict.update({key : machine_times})
        temp_machine = {machine_key : machine_inner_dict}
        machines.update(temp_machine)
    return machines

def generate_chromosome_list(num_of_chromosomes, jobs, machines, chromosomes):
    chromosome_list = []
    if len(chromosomes) != 0:
        for chromosome in chromosomes:
            chromosome_list.append(Chromosome(jobs, machines, chromosome))
    else:
        for i in range(num_of_chromosomes):    
            chromosome_list.append(Chromosome(jobs, machines, []))

    return chromosome_list

def get_chromosome_rang_dict(chromosomes_list, jobs, machines):
    data = {}
    for chromosome in chromosomes_list:
        data.update({chromosome : fitness_function(chromosome, machines, jobs, False)})

    #print("before sort : " + str(data))
    data_sorted = sorted(data.items(), key=lambda x:x[1])
    
    data.clear()
    for item in data_sorted:
        data.update({item[0] : item[1]})
    #print("after sort : " + str(data))
    best_unit = list(data)[-1]
    return data, best_unit

def rulette_selection(sorted_chromosome_dict):
    for key in sorted_chromosome_dict.keys():
        multiplyer = random.random()
        sorted_chromosome_dict[key] *= multiplyer
    
    data_sorted = sorted(sorted_chromosome_dict.items(), key=lambda x:x[1])
    
    #print("before sort : " + str(sorted_chromosome_dict))
    sorted_chromosome_dict.clear()
    for item in data_sorted:
        sorted_chromosome_dict.update({item[0] : item[1]})
    #print("after sort : " + str(sorted_chromosome_dict))
   
    list_of_pairs = []
    temp = []
    i = 0
    for key in sorted_chromosome_dict.keys():
        temp.append(key.chromosome)
        if (i + 1) % 2 == 0:
            list_of_pairs.append(temp)
            temp = []
        i += 1

    return list_of_pairs