import numpy as np
import matplotlib.pyplot as plt

width = 300
height = 200

bleu = [31, 119, 180]
gris = [127, 127, 127]
vert = [44, 160, 44]
orange = [255, 127, 14]

enveloppe = np.zeros((height, width, 3), dtype=np.uint8)

i = np.arange(height)
j = np.arange(width)

I, J = np.meshgrid(i, j, indexing="ij")

decroissante = ((2./3.) * J)
croissante = (height - (2./3.) * J)

ibleu = (I <= decroissante) & (I <= croissante)
igris = (I > decroissante) & (I <= croissante)
ivert = (I > decroissante) & (I > croissante)
iorange = (I <= decroissante) & (I > croissante)

enveloppe[ibleu] = bleu
enveloppe[igris] = gris
enveloppe[ivert] = vert
enveloppe[iorange] = orange


plt.imshow(enveloppe)
plt.show()