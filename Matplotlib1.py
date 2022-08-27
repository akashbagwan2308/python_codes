# saving plot file
import matplotlib.pyplot as plt
import pylab as pl

x= [0,2,4,6]
y = [1,3,4,8]
plt.plot(x,y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('plotted X and Y values')
plt.legend(['Data 1'])

# saving the plot
plt.savefig('plot1.png',dpi = 350, bbox_inches = 'tight')
plt.show()
