# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Resolution du cercle
qualite = 256

# tableau numpy d'affichage
render = np.zeros((qualite,qualite,3), dtype=np.uint8)

# Fonction qui permet de créer un quart de cercle
def cercle(render, r):
    global qualite
    # Boucle pour calculer l'image de chaque x
    # De haut en bas
    for ligne in range(qualite):
        # x est egale
        x = qualite - ligne
        # calcul du pixel limite
        limite = int(np.sqrt(r * r - x * x))
        render[ligne:ligne+1,0:limite,:] = [255,90,45]


cercle(render, qualite)
plt.imshow(render)
plt.show()
