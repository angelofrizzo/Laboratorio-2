import csv
import numpy as np

lst = []

with open("angelofrizzo/Laboratorio-2/resistenza2/resistenza2_0.csv", newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for line in data:
            for x in line:
                lst.append(float(x))

    dati = np.array(lst)

print(dati)