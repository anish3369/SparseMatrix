from scipy.io import mmread
from matplotlib import pyplot as plt
import numpy as np
raw_data = mmread("1138_bus.mtx")
raw_data
ex_2 = raw_data.toarray()
y = ex_2[ex_2.nonzero()]
x = [i for i in range(1,len(y)+1)]
plt.plot(x,y)
plt.show()
