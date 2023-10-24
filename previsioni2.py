import numpy as np
import matplotlib.pyplot as plt

resistente = [147.23e3, 67.67e3]
condensatore = 32.9e-9

frequenze = np.logspace(np.log10(10000), np.log10(100000), 10)

print(frequenze)

frequenze = np.array([
    10000,
    11500,
    13000,
    13500,
    14000,
    14250,
    14500,
    15500,
    17000,
    21500,
    30000,
    60000
])

V_in = np.array([
    3.560,
    3.540,
    3.540,
    3.540,
    3.540,
    3.540,
    3.540,
    3.540,
    3.540,
    3.560,
    3.540,
    3.540
])

V_out = np.array([
    0.030,
    0.052,
    0.180,
    0.352,
    0.316,
    0.224,
    0.1568,
    0.101,
    0.042,
    0.0205,
    0.01088,
    0.000456
])

fase = np.array([
    86,
    83,
    67,
    36,
    -44,
    -57
    -68,
    -76,
    -82,
    -87,
    -87,
    -87
])


plt.scatter(frequenze, V_out/V_in)
plt.xscale("log")
plt.yscale("log")
plt.show()
