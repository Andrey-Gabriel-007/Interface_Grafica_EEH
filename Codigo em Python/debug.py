from EEH import EEH
import numpy as np
import random
med_tensao = np.zeros(34, dtype=int)
med_corrente = np.zeros(66, dtype=int)
for k in range(10000):  
    print('teste numero' , k)
    for i in range(34):
        med_tensao[i] = random.randint(0, 1)

    for j in range(66):
        med_corrente[j] = random.randint(0, 1)
    EEH(med_tensao, med_corrente)