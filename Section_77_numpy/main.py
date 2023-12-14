import numpy as np
import matplotlib.pyplot as pyplot
from PIL import Image

one_d_array = np.array([1, 2, 3])
print(one_d_array.shape)
print(one_d_array.ndim)

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d_array.shape)
print(two_d_array.ndim)
print(two_d_array[1, 0])
print(two_d_array[0, :])
print(two_d_array[:, 1])
