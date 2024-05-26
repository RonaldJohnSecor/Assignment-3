#Example 1: Load from a Text File
import numpy as np

data = np.loadtxt('data.txt')
print(data)

print()
#Example 2: Load from a Binary File
import numpy as np

data = np.load('data.npy')
print(data)

print()
#Example 3: Load from a Compressed File
import numpy as np

loaded = np.load('data_compressed.npz')
data = loaded['arr_0']
print(data)