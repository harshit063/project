import numpy as np
import pandas as pd
import random
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
time = ['9:15-10:15','10:15-11:15','11:15-12:15','12:45-2:45','2:45-4:45']
subject_theory = ['OPC','SM','PD.L','FM']
subject_practical = ['PD(PRAC)','LAB.IOT(PRAC)','MAJOR PROJECT']
TT = pd.DataFrame(np.nan,index = range(5),columns = range(5))
TT.index = days
TT.columns = time

TT = pd.DataFrame(np.nan,index = range(5),columns = range(5))
TT.index = days
TT.columns = time

def subject_remove():
    for i in range(len(subject_theory)):
        count_theory =np.count_nonzero(arr_TT == subject_theory[i])
        if count_theory == 3:
            return subject_theory.remove(subject_theory[i])
    for i in range(len(subject_practical)):
        count_practical =np.count_nonzero(arr_TT == subject_practical[i])
        if count_practical ==2:
            return subject_practical.remove(subject_practical[i])

for i in range(5):
    for j in range(5):
        if i == 0:
            subject_theory = ['OPC','SM','PD.L','FM']
            TT.iloc[[i],[j]] = random.choice(subject_theory)
            if j>2:
                subject_practical = ['PD(PRAC)','LAB.IOT(PRAC)','MAJOR PROJECT']
                TT.iloc[[i],[j]] = random.choice(subject_practical)
        arr_TT = TT.to_numpy()
        subject_remove()
        if i == 1:
            TT.iloc[[i],[j]] = random.choice(subject_theory)
            if j>2:
                TT.iloc[[i],[j]] = random.choice(subject_practical)
        arr_TT = TT.to_numpy()
        subject_remove()
        if i ==2:
            TT.iloc[[i],[j]] = random.choice(subject_theory)
            if j>2:
                TT.iloc[[i],[j]] = random.choice(subject_practical)
        arr_TT = TT.to_numpy()
        subject_remove()
        if i ==3:
            TT.iloc[[i],[j]] = random.choice(subject_theory)
            if j>2:
                TT.iloc[[i],[j]] = random.choice(subject_practical)
        arr_TT = TT.to_numpy()
        subject_remove()

        if i ==4:
            if j<=2:
                TT.iloc[[i],[j]] = random.choice(subject_theory)
            if j>2:
                TT.iloc[[i],[j]] = random.choice(subject_practical)
        arr_TT = TT.to_numpy()
        subject_remove()
        print(TT)