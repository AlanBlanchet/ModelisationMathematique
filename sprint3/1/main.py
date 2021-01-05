# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import math as math

np.set_printoptions(suppress=True)

face = plt.imread('../face.png', 'PNG');
l, c, colFormat = face.shape

plan = np.ones(face.shape, dtype=np.uint8) * 200
u = (-300,-150)

# Obtention du centre des pixels
cPixelsH = np.linspace(0.5, c - 0.5, c)
cPixelsV = np.linspace(l - 0.5, 0.5, l)
X, Y = np.meshgrid(cPixelsH,
                   cPixelsV, 
                   indexing='xy')

I, J = np.meshgrid(np.arange(c, -1, -1),
                   np.arange(l),
                   indexing="ij")

def translater(v):
  global plan
  # Conversion du vecteur pour avoir (0,0) en bas à gauche
  v = (v[0],-v[1])
  for colonne in range(c):
    for ligne in range(l):
      pixel = (colonne - v[0], ligne - v[1])
      if(pixel[0] < c and pixel[0] >= 0 and pixel[1] < l and pixel[1] >= 0):
        plan[ligne,colonne] = face[pixel[1],pixel[0]]

def homotetie(v, rapport):
  global plan
  # Conversion de v pour avoir (0,0) en bas à gauche
  v[1] = l - v[1]
  for colonne in range(c):
    for ligne in range(l):
      ligne += 0.5
      colonne += 0.5
      vDist = (colonne, ligne) - v
      vAntecedant = vDist / rapport
      pixel = vAntecedant + v
      pixel = pixel.astype(int)
      
      if(pixel[0] < c and pixel[0] >= 0 and pixel[1] < l and pixel[1] >= 0):
        plan[ligne,colonne] = face[pixel[1],pixel[0]]

def rotation(v, angle):
  global plan
  # Conversion de v pour avoir (0,0) en bas à gauche
  v[1] = l - v[1]
  # Conversion car axe inversé
  angle = -angle
  print v[0]
  print v[1]
  for colonne in range(c):
    for ligne in range(l):
      somme = np.array([
          (1.0-math.cos(angle)*v[0]+math.sin(angle)*v[1]),
          (-math.sin(angle)*v[0]+(1.0 - math.cos(angle))*v[1])
      ])
      matTrans = np.array([[math.cos(angle), -math.sin(angle)],
                        [math.sin(angle), math.cos(angle)]])
      invMatTrans = inv(matTrans)
      pixel = ((colonne, ligne) - somme).dot(invMatTrans)
      pixel = pixel.astype(int)
      
      if(pixel[0] < c and pixel[0] >= 0 and pixel[1] < l and pixel[1] >= 0):
        plan[ligne,colonne] = face[pixel[1],pixel[0]]
  
# HOMOTETIE
# 1
# homotetie(np.array([0,0]), math.sqrt(2))
# 2
# homotetie(np.array([0,0]), 1 / math.sqrt(2))
# 3
# homotetie(np.array([c / 2, l / 2]), 2)
# 4
#homotetie(np.array([c / 2, l / 2]), 1 / math.sqrt(2))

# ROTATION
# 1
# rotation(np.array([0,0]), math.pi / 6)
# 2
# rotation(np.array([0,0]), -math.pi / 6)
# 3
rotation(np.array([512.0,384.0]), math.pi / 2)
# 4
# rotation(np.array([0,0]), math.pi / 6)


plt.imshow(plan)
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