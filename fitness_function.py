def fitness_function(chromosome, machines, jobs, is_elitis):
    """
    chromosome - predstavlja jednu jedinku tojest jedan hromozom
    on je u formatu [[][]] lista koja sadrzi u sebi 2 liste
    u prvoj listi nalaze se informacije o redosledu izvrsavanja poslova tojest operacija
    u drugoj listi nalaze se informacije o redosledu masina

    machines - predstavlja dictionary masina a svaki element predstavlja masinu koja je dictionary
    koji sadrzi informacije za svaki posao i za trajanje operacije u tom poslu kao i koliko ima tih operacija

    jobs - predstavlja listu poslova, samo broj poslova

    Potrebno je proci kroz gen koji sadrzi informacije o redosledu poslova 
    onoliko puta koliko ima poslova
    Za svaki posao gleda se redosled operacija i redosled masina i sastavlja se vreme za 
    svaku masinu posebno

    return vrednost funkcije je najgore/najduze vreme izvrsavanja svih masina

    """
    if isinstance(chromosome, list):
        jobs_c = chromosome[0]
        machines_c = chromosome[1]
    else:
        jobs_c = chromosome.chromosome[0]
        machines_c = chromosome.chromosome[1]

    times = {}

    # for i in range(len(machines)): # postavlja svako vreme rada masine na nula u times
    #     machine = "M" + str(i + 1)
    #     times[machine] = 0

    machine_names = machines.keys() # ovo je drugi nacin koji je vrv bolji
    for i in machine_names:
        times[i] = 0
    
    for i in range(len(jobs)):
        curren_job = jobs_c[i]
        p = 0 #pozicija u masinama hromozoma
        o = 0 #broj operacije po redu u hromozomu
        used_machines = [] #masine koje su koriscene za jedan posao
        durations = [] #duzine procesa redom
        total_duration = 0
        for job in jobs_c:
            if job == curren_job:
                machine = machines_c[p] #masina koja se koristi za tu operaciju u hromozomu
                process_duration = machines[machine][job][o]
          
                #potrebno je inkrementirati vreme masine u dictionaryju times

                if (o == 0): #ukoliko je to prva operacija onda se na masinu samo dodaje vreme
                    times[machine] += process_duration
                else: #ukoliko nije prva operacija onda se gleda razlika vremena izmedju masina
                    if (machine not in used_machines): #ukoliko su prethodni procesi bili na razlicitim masinama
                        times[machine] += process_duration
                    # elif (machine in used_machines): #ukoliko su bili ni jednom ili vise puta na trenutnoj masini
                    #     times[machine] += process_duration
                    else:
                        for u in range(len(used_machines)):
                            if machine == used_machines[u]:
                                times[machine] -= durations[u]
                        times[machine] += total_duration                        

                o += 1 #povecanje operacije mora biti u ifu jer se povecava samo ukoliko je trenutni job = jobu iz hromozoma
                used_machines.append(machine)
                total_duration += process_duration
                durations.append(process_duration)
            p += 1 #pozicija hromozoma se povecava prilikom svake iteracije

                
    finish_time = max(times.values())
    return finish_time


# jobs = ParameterFns.generate_Jobs(2, 3)
# mashines = ParameterFns.generate_Machines(3, jobs, 10)

# print("jobs = " + str(jobs))
# print("machines = " + str(mashines))

# chromosome = Chromosome.generate_chromosome(jobs, mashines)
# print("machines = " + str(chromosome))

# time = fitness_function(chromosome, mashines, jobs)
# print(time)