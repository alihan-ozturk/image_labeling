import numpy as np


path = "path/labels_array.npy"
data = np.load(path)
print(data)
print(data.shape)