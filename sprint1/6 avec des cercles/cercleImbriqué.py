# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

l = 300
h = 200
rayonMax = 80
rayonMin = 70

orange =[255, 127, 14]
bleu = [31, 119, 180]
vert = [44, 160, 44]

cercles = np.ones((h, l, 3), dtype=np.uint8) * np.array(bleu, dtype=np.uint8)

I, J = np.meshgrid(np.arange(h), 
                   np.arange(l),
                   indexing='ij')
cOrange = (200,100)
cVert = (100, 100)

iDonutOrangeDist = np.sqrt((I - cOrange[1]) ** 2 + ((J - cOrange[0]) ** 2 ))
iDonutOrangeMin = (rayonMin) < (iDonutOrangeDist)
iDonutOrangeMax = (rayonMax) > (iDonutOrangeDist)
iDonutOrange = iDonutOrangeMin & iDonutOrangeMax

iDonutVertDist = np.sqrt((I - cVert[1]) ** 2 + ((J - cVert[0]) ** 2 ))
iDonutVertMin = (rayonMin) < (iDonutVertDist)
iDonutVertMax = (rayonMax) > (iDonutVertDist)
iDonutVert = iDonutVertMin & iDonutVertMax

# (I < h + 1) Permet d'avoir un tableau de boolean avec toute ses valeurs vraies
iOmegaPriveInterBas = (I < h + 1) ^ (iDonutVert & iDonutOrange & (I > 100))
iDonutVert = iDonutVert & iOmegaPriveInterBas


cercles[iDonutOrange, :] = orange
cercles[iDonutVert, :] = vert

plt.imshow(cercles)
plt.show()
