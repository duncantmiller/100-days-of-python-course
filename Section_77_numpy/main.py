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
reversed_a = np.flip(a)
print(reversed_a)

b = [6,0,9,0,0,5,0]
print(np.nonzero(b)[0].tolist())

rng = np.random.default_rng()
array_a = rng.integers(low=0, high=10, size=27)
print(array_a)
tensor_a = array_a.reshape(3, 3, 3)
print(tensor_a)
print(tensor_a.shape)

spaced_x = np.linspace(0, 100, num=9)
print(spaced_x)
spaced_y = np.linspace(-3, 3, num=9)
print(spaced_y)
# pyplot.plot(spaced_x, spaced_y)
# pyplot.show()

noise = np.random.rand(128, 128, 3)
print(noise)
