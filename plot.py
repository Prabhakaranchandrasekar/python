import matplotlib.pyplot as plt
import numpy as np
xaxis=np.array([0,2,4,6,8,10,12])
yaxis=np.array([4,2,6,2,8,4,10])
plt.title("trend")
plt.xlabel("month")
plt.ylabel("range")
plt.plot(xaxis,yaxis,'o:r')
plt.show()

