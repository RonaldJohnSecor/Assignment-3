#Example 1: Save to a Text File
import numpy as np

data = np.array([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
np.savetxt('data.txt', data)


#Example 2: Save to a Binary File
import numpy as np

data = np.array([1, 2, 3, 4, 5])
np.save('data.npy', data)


#Example 3: Save to a Compressed File
import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
np.savez_compressed('data_compressed.npz', data)