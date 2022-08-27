# Multi line plot
# Object oriented interface
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)
# t = np.tan(x)
fig, ax = plt.subplots()
ax.plot(x,y)
ax.plot(x,z)
# ax.plot(x,t)
ax.set_title('Two trigo functions')
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle')
ax.yaxis.set_label_text('Sine And Cosine')

plt.savefig('plot2.png',dpi = 400,bbox_inches = 'tight')
plt.show()
