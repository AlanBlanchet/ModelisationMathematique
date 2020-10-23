# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

orange =[255,127,14]
bleu = [31,119,180]

rayon = 200

quart = np.ones((200,200,3), dtype=np.uint8) * np.array(bleu, dtype=np.uint8)

x = np.linspace(-199.5, 199.5, 200)       
y = np.linspace(-199.5, 199.5, 200)    

X, Y = np.meshgrid(x,y)
print X

quart[rayon >= np.sqrt(X * X + Y * Y)] = orange

plt.imshow(quart)
plt.show()
