from re import X
import matplotlib.pyplot as pit
import numpy as np

x = np.linspace(0,20,100)
pit.plot(x , np.sin(x))
pit.show()