#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
qualite = 256

render = np.zeros((qualite,qualite,3), dtype=np.uint8)
for x in range(qualite):
    render[x-1:x,x-1:x,:] = [255,90,45]
    
plt.imshow(render)
plt.show()