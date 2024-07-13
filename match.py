import matplotlib.pyplot as plt
import numpy as np
xaxis=np.array([1,2,3,4,5,6,7,8])
yaxis=np.array([2010,2014,2015,2016,2019,2020,2022,2024])
plt.title("Cricket")
plt.xlabel("Matches")
plt.ylabel("2010-2024")
plt.plot(xaxis,yaxis,'o')
plt.show()