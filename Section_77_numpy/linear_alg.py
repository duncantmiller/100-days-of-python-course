import numpy as np
import matplotlib.pyplot as pyplot
from PIL import Image

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)
print(v1 * v2)
print(v1 * 2)

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(a1 @ b1)
print(np.matmul(a1, b1))

image = Image.open('yummy_macarons.jpg')

pyplot.imshow(image)
pyplot.show()
