import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])

plt.plot(x,y)

x1 = [2,4,6,8]
y1=[3,5,7,9]

plt.plot('x-axis data')
plt.xlabel('x-axis data')
plt.ylabel('y-axis data')
plt.title('multiple plots')

plt.fill_between(x,y,y1,color='green';alpha=0.5)
plt.show()