# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = int(input("Choisissez le photomaton :\n1 = doubler horizontal\n2 = double vertical\n3 = quadruple\n:"))

cheval = plt.imread("../../images/dark-knight.png","PNG")

def horizontal():
    global cheval
    cheval = np.block([[cheval], [cheval]])

def vertical():
    global cheval
    cheval = np.block([[[cheval]], [[cheval]]])

if x == 1:
    horizontal()
elif x == 2:
    vertical()
elif x == 3:
    horizontal()
    vertical()

plt.imshow(cheval)
plt.show()