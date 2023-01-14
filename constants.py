from ParameterFns import *

#moze da se napravi random
# jobs = ParameterFns.generate_Jobs(2, 3)
# machines = ParameterFns.generate_Machines(3, jobs, 10)

# chromosome_list = ParameterFns.generate_chromosome_list(4, jobs, machines)

JOBS = generate_Jobs(2, 3)
JOBS_KEYS = list(JOBS.keys())
MACHINES = generate_Machines(3, JOBS, 10)
CHROMOSOMES = generate_chromosome_list(4, JOBS, MACHINES)