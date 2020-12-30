import numpy as np
import matplotlib.pyplot as plt

width = 300
height = 200

bleu = [31, 119, 180]
gris = [127, 127, 127]
vert = [44, 160, 44]
orange = [255, 127, 14]

x = np.arange(width)
y = np.arange(height - 1, -1, -1)

X, Y = np.meshgrid(x, y)

y1 = np.linspace(2/3, height, width)
y2 = np.linspace(height, 2/3, width)

enveloppe = np.zeros((height, width, 3), dtype = np.uint8)


ibleu = (y2 <= Y) & (y1 <= Y)
igris = (y2 > Y) & (y1 < Y)
ivert = (y2 > Y) & (y1 > Y)
iorange = (y2 <= Y) & (y1 > Y)

enveloppe[ibleu,:] = bleu
enveloppe[igris,:] = gris
enveloppe[ivert,:] = vert
enveloppe[iorange,:] = orange

plt.imshow(enveloppe)
plt.show()