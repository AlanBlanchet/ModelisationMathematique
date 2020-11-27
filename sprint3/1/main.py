# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

face = plt.imread('../face.png', 'PNG');
l, c, colFormat = face.shape

gris = [200,200,200];

carreGris = np.ones((l, c, colFormat), dtype=np.uint8) * np.array(gris, dtype=np.uint8)

u = (150,150)

X, Y = np.meshgrid(np.arange(c),
                   np.arange(l), 
                   indexing='xy')

#lFace = (()face - u[1])) > 0 && ((face - u[1]) < l)

#print(lFace)

for j in range(l):
     for i in range(c):
         decalageI = i + u[0]
         decalageJ = j - u[1]
         if(decalageJ > 0 and decalageJ < l and decalageI > 0 and decalageI < c):
             carreGris[decalageJ,decalageI] = face[j,i]

plt.imshow(carreGris)
plt.show()


# 1 - Méthode avec des boucles
# for j in range(l):
#     for i in range(c):
#         decalageI = i + u[0]
#         decalageJ = j - u[1]
#         if(decalageJ > 0 and decalageJ < l and decalageI > 0 and decalageI < c):
#             carreGris[decalageJ,decalageI] = face[j,i]

# 2 - Slicing
# On récupère l'interval de gris à modifier
# carreGrisJDeb = (0,-u[1])[u[1] < 0]
# carreGrisJFin = (l - u[1], l)[u[1] < 0]
# carreGrisIDeb = (u[0],0)[u[0] < 0]
# carreGrisIFin = (c, c + u[0])[u[0] < 0]

# On récupère l'interval de l'image à modifier
# faceJDeb = (u[1], 0)[u[1] < 0]
# faceJFin = (l, l + u[1])[u[1] < 0]
# faceIDeb = (0, -u[0])[u[0] < 0]
# faceIFin = (c - u[0], c)[u[0] < 0]

# On effectue la translation
# carreGris[carreGrisJDeb:carreGrisJFin, carreGrisIDeb:carreGrisIFin] = face[faceJDeb:faceJFin, faceIDeb:faceIFin]