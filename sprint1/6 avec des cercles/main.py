# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

render = np.zeros((50,50,3), dtype=np.uint8)

def cercle(render, r):
    for x in range(50):
        bord = np.sqrt(r * r - x * x)
        render[bord:bord,x:x,:] = [255,0,0]

plt.imshow(render)
plt.show()