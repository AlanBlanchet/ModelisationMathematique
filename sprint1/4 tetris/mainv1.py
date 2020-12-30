# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#code RVB des couleurs présentent sur l'image finale
bleu = [31,19,180]
orange = [255,127,14]
vert = [44,160,44]

#sélection de l'étape souhaitée
rendu = np.ones((200,300,3), dtype=np.uint8) * 127

I, J = np.meshgrid(np.arange(200),
                   np.arange(300),
                   indexing="ij")

iBleu = J < 50
iVertP1 = (I >= 150) & (J < 250) & (J >= 150)
iVertP2 = (I >= 100) & (I < 150) & (J >= 200)
iVert = iVertP1 | iVertP2

# Etape 1
iOrangeE1P1 = (J >= 50) & (J < 100) & (I < 150)
iOrangeE1P2 = (I >= 50) & (I < 100) & (J < 150) & (J >= 100)
iOrangeE1 = iOrangeE1P1 | iOrangeE1P2
# Etape 2
iOrangeE2P1 = (I >= 50) & (I < 100) & (J >= 50) & (J < 200)
iOrangeE2P2 = (I >= 100) & (I < 150) & (J >= 100) & (J < 150)
iOrangeE2 = iOrangeE2P1 | iOrangeE2P2
# Etape 3
iOrangeE3P1 = (I >= 100) & (I < 150) & (J >= 50) & (J < 200)
iOrangeE3P2 = (I >= 150) & (J >= 100) & (J < 150)
iOrangeE3 = iOrangeE3P1 | iOrangeE3P2

rendu[iBleu] = bleu
rendu[iVert] = vert
rendu[iOrangeE3] = orange

plt.imshow(rendu)
plt.show()