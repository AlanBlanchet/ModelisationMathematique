import numpy as np
import matplotlib.pyplot as plt

width = 300
height = 200

x = np.arange(width)
y = np.arange(height - 1, -1, -1)

X, Y = np.meshgrid(x, y)

y1 = np.linspace(2/3, height, width)
y2 = np.linspace(height, 2/3, width)

enveloppe = np.zeros((height, width, 3), dtype = np.uint8)

enveloppe_bleue = (y2 < Y) & (y1 < Y)
enveloppe_gris = (y2 > Y) & (y1 < Y)


enveloppe[(y2 < Y) & (y1 < Y),:] = [31, 119, 180]
enveloppe[(y2 > Y) & (y1 < Y),:] = [127, 127, 127]
enveloppe[(y2 > Y) & (y1 > Y),:] = [44, 160, 44]
enveloppe[(y2 < Y) & (y1 > Y),:] = [255, 127, 14]
enveloppe[199,299] = [255, 127, 14]

plt.imshow(enveloppe)
plt.show()