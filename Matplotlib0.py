# matplotlib for data visualization
import matplotlib
print(matplotlib._get_version())
# Line Plots
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1 )
y = np.sin(x)
plt.plot(x,y)
plt.show()
# y = x*x + 5*x +2
# plt.plot(x,y)
# plt.show()
