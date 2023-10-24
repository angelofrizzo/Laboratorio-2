import numpy as np

resistenze = np.array([215.07, 117.97, 324.59, 575.12, 465.16])
tau10 = np.array([232e-7, 424e-7, 154e-7, 87e-7, 107e-7])

for i in tau10:
    print("Tau10 di {tau}".format(tau = i*10))