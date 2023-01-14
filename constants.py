from ParameterFns import *

JOBS = generate_Jobs(6, 2)
JOBS_KEYS = list(JOBS.keys())
MACHINES = generate_Machines(5, JOBS, 20)
CHROMOSOMES = generate_chromosome_list(4, JOBS, MACHINES, [])