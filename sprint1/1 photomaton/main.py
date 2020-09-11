# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

finalTab = np.zeros((180,180,4))

cheval = plt.imread("dark-knight.png","PNG")
finalTab = np.copy(cheval)
tab2 = np.copy(cheval)
img = np.block([finalTab, tab2])
print(img)
print(img.shape)
plt.imshow(img)
plt.show()
