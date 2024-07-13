# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3])
# y=np.array([4,5,6])
# z=np.array([3,4,3,5,3,4])
# l=np.concatenate((x,y))
# print(l)
# plt.plot(l,z,'o:g')
# plt.show()
#
# import numpy as np
# arr1=np.array([1,2,3,4,5,4,4])
# x=np.where(arr1==4)
# print(x)

# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.stack((arr1,arr2),axis=1)
# print(arr)

# import numpy as np
# arr1=np.array([1,2,3,4,5,4,4])
# x=np.where(arr1%2==0)
# print(x)

# import numpy as np
# arr1=np.array([1,2,3,4,5,4,4])
# x=np.searchsorted(arr1,5)
# print(x)

# import numpy as np
# arr1=np.array([1,2,3,4,5,4,4])
# x=np.searchsorted(arr1,5,side='right')
# print(x)

# import numpy as np
# arr=np.array([1,3,5,7])
# x=np.searchsorted(arr,[2,4,6,8])
# print(x)

# import numpy as np
# arr=np.array([7,8,5,2,3,1])
# x=np.sort(arr)
# print(x)

# import numpy as np
# arr=np.array([41,42,43,44])
# filter_arr=[]
# for element in arr:
#     if element>42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
# new_arr=arr[filter_arr]
# print(filter_arr)
# print(new_arr)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# filter_arr=[]
# for element in arr:
#     if element%2==0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
# new_arr=arr[filter_arr]
# print(filter_arr)
# print(new_arr)

# from numpy import random
# x=random.rand()
# print(x)

from numpy import random
x=random.randint(10,size=(4))
print(x)