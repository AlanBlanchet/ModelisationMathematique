# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Fonctions
def collerHorizontal(img1, img2):
    return np.block([[img1], [img2]])

def collerVertical(img1, img2):
    return np.block([[[img1]], [[img2]]])

def flipHorizontal(img):
    return img[:,::-1]

def flipVertical(img):
    return img[::-1]

def repeterHorizontal(img, n):
    if n <= 1: return img;
    return np.block([[img], [repeterHorizontal(img, n - 1)]])
  
def repeterVertical(img, n):
    if n <= 1: return img;
    return np.block([[[img]], [[repeterVertical(img, n - 1)]]])

# Variables et appels
carre = np.zeros((20,20,3), dtype=np.uint8)

# On insère du orange dans le carré
carre[:,:,:] = [255, 127, 14]
# On insère du vert en bas à droite de la 14e ligne à la dernière
# et de la 14e colonne à la dernière
carre[14:,14:,:] = [44, 160, 44]

# On execute la fonction pour coller le carré et son image horizontale
carre = collerHorizontal(carre, flipHorizontal(carre))
# On execute la fonction pour coller le carré et son image verticale
carre = collerVertical(carre, flipVertical(carre))

# On répète le carré 3 fois horizontalement
carre = repeterHorizontal(carre, 3)
# On répète le carré 3 fois verticalement
carre = repeterVertical(carre, 2)

plt.imshow(carre)
plt.show()