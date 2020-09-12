# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = int(input("Choisissez le flip :\n1 = flip horizontal\n2 = flip vertical\n3 = quadruple avec flip vertical\n:"))

cheval = plt.imread("../../images/dark-knight.png","PNG")

def doubleHorizontal(img):
    return np.block([[img], [img]])

def doubleVertical(img):
    return np.block([[[img]], [[img]]])

def flipHorizontal(img):
    return img[:,::-1]

def flipVertical(img):
    return img[::-1]

if x == 1:
    cheval = flipHorizontal(cheval)
elif x == 2:
    cheval = flipVertical(cheval)
elif x == 3:
    flipV = flipVertical(cheval)
    cheval = np.block([[[cheval]],[[flipV]]])
    cheval = doubleHorizontal(cheval)
else:
    print("Ce n'est pas une option.")

plt.imshow(cheval)
plt.show()