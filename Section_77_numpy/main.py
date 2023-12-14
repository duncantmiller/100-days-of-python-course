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

tensor = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
)
print(tensor.shape)
print(tensor.ndim)
print(tensor[0, 0, 0])
print(tensor[1, 1, 2])
print(tensor[1, 1, :])
print(tensor[:, :, 0])

a = np.arange(10, 30)
print(a)

sub_a_last_three = a[17:]
print(sub_a_last_three)
sub_a_last_eight = a[12:]
print(sub_a_last_eight)
sub_a_even = a[::2]
print(sub_a_even)
