#Creating a NumPy Array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#2D Array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
#Zeros, Ones and Identity
import numpy as np
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.eye(3))
#arange()
import numpy as np
arr = np.arange(1, 11, 2)
print(arr)
#Copy and View
import numpy as np
arr = np.array([10, 20, 30])
view_arr = arr.view()
view_arr[0] = 100
print(arr)