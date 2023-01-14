from constants import *

def average_value(list_of_values):
    average = sum(list_of_values) / len(list_of_values)
    return average

def raspored(the_best):

    poslovi = the_best[0]
    masine = the_best[1]

    masine_vremena = {}
    masine_posebno_rad = {}
    for i in range(len(MACHINES)):
        masine_vremena [list(MACHINES.keys())[i]] = 0
        masine_posebno_rad [list(MACHINES.keys())[i]] = 0

    for i in range(len(list(JOBS_KEYS))):
        curren_job = poslovi[i]
        p = 0 #pozicija u masinama hromozoma
        o = 0 #broj operacije po redu u hromozomu
        used_machines = [] #masine koje su koriscene za jedan posao
        durations = [] #duzine procesa redom
        total_duration = 0
        for job in poslovi:
            if job == curren_job:
                machine = masine[p] #masina koja se koristi za tu operaciju u hromozomu
                process_duration = MACHINES[machine][job][o]
          
                #potrebno je inkrementirati vreme masine u dictionaryju times

                if (o == 0): #ukoliko je to prva operacija onda se na masinu samo dodaje vreme
                    masine_vremena[machine] += process_duration
                else: #ukoliko nije prva operacija onda se gleda razlika vremena izmedju masina
                    if (machine not in used_machines): #ukoliko su prethodni procesi bili na razlicitim masinama
                        masine_vremena[machine] += process_duration
                    # elif (machine in used_machines): #ukoliko su bili ni jednom ili vise puta na trenutnoj masini
                    #     times[machine] += process_duration
                    else:
                        for u in range(len(used_machines)):
                            if machine == used_machines[u]:
                                masine_vremena[machine] -= durations[u]
                        masine_vremena[machine] += total_duration                        

                o += 1 #povecanje operacije mora biti u ifu jer se povecava samo ukoliko je trenutni job = jobu iz hromozoma
                used_machines.append(machine)
                total_duration += process_duration
                durations.append(process_duration)
                masine_posebno_rad[machine] = durations
            p += 1 #pozicija hromozoma se povecava prilikom svake iteracije

    return masine_vremena, masine_posebno_rad

def redosled_operacija(the_best):
    poslovi = the_best[0]
    masine = the_best[1]
    masine_poslovi = {}
    for i in range(len(MACHINES)):
        masine_poslovi[list(MACHINES.keys())[i]] = []

    for i in range(len(masine)):
        masina = masine[i]
        masine_poslovi[masina].append(poslovi[i])

    return masine_poslovi
