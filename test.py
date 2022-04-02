import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

a = [1,2,3]
b = [1,2,3]
c = [3,3,3]
d = [1,2,3]

fig1, ax1 = plt.subplot(figsize=(96,48))
ax1.plot(a, b)

ax2 = plt.subplot(figsize=(96,48))
ax2.plot(c, d)

plt.show()