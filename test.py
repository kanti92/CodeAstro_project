import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sea

print('Hello')

x = np.arange(29)

y = []
for __, item in enumerate(x):
    y_value = item + 2*item
    y.append(y_value)


fig, ax = plt.subplots()
plt.plot(x,y,)
plt.show()