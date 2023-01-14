import random
from constants import *

def crossover(pairs):

    """
    pairs - lista koja sadrzi 2 hromozoma u listi kao par mame i tate

    deca nastaju na sledeci nacin:
    1. dete = poslovi od mame (prva komponenta u hromozomu) + redosled masina od tate (druga komponenta u hromozomu)
    2. dete = poslovi od tate (prva komponenta u hromozomu) + redosled masina od mame (druga komponenta u hromozomu)

    treba voditi racuna da je redosled masina kod dece moguc

    povratna vrednost funckije su 2 liste, jedna sa roditeljima, jedna sa decom

    """

    children = []
    parents = []
    for pair in pairs:
        child1 = []
        child2 = []
        mom = pair[0]
        dad = pair[1]

        child1.append(mom[0])
        child1.append(dad[1])

        child2.append(dad[0])
        child2.append(mom[1])

        #provera ispravnosti redosleda masina u detety
        for j in range(len(JOBS_KEYS)): #za 1. dete
                o = 0
                for i in range(len(mom[1])):
                    job = child1[0][i]
                    machine = child1[1][i]

                    if job == JOBS_KEYS[j]:
                        proces_duration = MACHINES[machine][job][o]
                        if MACHINES[machine][job][o] == 0:
                            #ukoliko je 0 onda mora da pronadje masinu koja radi
                            while proces_duration != 0:
                                new_m = random.choice(MACHINES.keys())
                                proces_duration = MACHINES[machine][job][o]
                                child1[1][i] = new_m

        for j in range(len(JOBS_KEYS)): #za 2. dete
                o = 0
                for i in range(len(mom[1])):
                    job = child2[0][i]
                    machine = child2[1][i]

                    if job == JOBS_KEYS[j]:
                        proces_duration = MACHINES[machine][job][o]
                        if MACHINES[machine][job][o] == 0:
                            #ukoliko je 0 onda mora da pronadje masinu koja radi
                            while proces_duration != 0:
                                new_m = random.choice(MACHINES.keys())
                                proces_duration = MACHINES[machine][job][o]
                                child2[1][i] = new_m

        #dodavanje dece u listu deca
        #dodavanje roditelja u listu roditelja
        children.append(child1)
        children.append(child2)
        parents.append(mom)
        parents.append(dad)
    return children, parents