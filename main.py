from constants import *
import Genetic_Algorithm
import matplotlib.pyplot as plt
import numpy as np
from Graphic_helper import raspored, redosled_operacija

chromosomes, the_best, values, ya, yb = Genetic_Algorithm.genetic(100)
x = np.linspace(0, len(ya), len(ya))


plt.plot(x, yb, label="najbolja vrednost")
plt.scatter(x, ya, label="prosecna vrednost", color="orange")
plt.title("Genetski algoritam")
plt.xlabel("Generacije")
plt.ylabel("Vrednosti izrazene u jedinici vremena")
plt.legend()
plt.show()


redosled = redosled_operacija(the_best)
print(redosled)

plt.plot(5,5, label=str(redosled))
plt.legend()
plt.show()