# import numpy
# a=numpy.array([10,20,30,40,50,60])
# print(a)

# import numpy as np
# a=np.array([[10,20,30],[40,50,60]])
# print(type(a))
# print(a)

# import numpy as np
# a=np.array([[10,20,30]+[40,50,60]])
# print(a)
#
#
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr[0:5:2])
#
# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:2])

# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:2,2:4])

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# print(a.ndim)
# print(a[0:2])

# import numpy as np
# a=np.array([1,2,3,4],ndmin=2)
# print(a)
# print(a.ndim)

# import numpy as np
# arr=np.array([[1,2,3,4],[6,7,8,9]])
# print(arr.dtype)
#
# import numpy as np
# arr=np.array([1,2,3,4,6,7,8,9])
# a=arr.copy()
# b=arr.view()
# print(arr)
# print(a)
# print(b)

# import numpy as np
# arr=np.array([[1,2,3,4],[6,7,8,9]])
# print(arr.shape)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10])
# a=arr.reshape(2,5)
# print(a)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a=arr.reshape(2,3,2)
# print(a)

# import numpy as np
# arr=np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13]])
# for x in arr:
#     for y in x:
#       print(y)

# import numpy as np
# arr=np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13]])
# for x in np.nditer(arr):
#  print(x)

# import numpy as np
# arr=np.array([1,2,3,4])
# for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
#  print(x)

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::3]):
 print(x)


