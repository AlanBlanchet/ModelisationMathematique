# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def flipHorizontal(img):
    return img[:,::-1]

def flipVertical(img):
    return img[::-1]

def collerHorizontal(img1, img2):
    return np.block([[img1], [img2]])

def collerVertical(img1, img2):
    return np.block([[[img1]], [[img2]]])

orange =[255,127,14]

rayon = 200

quart = np.ones((200,200,3), dtype=np.uint8) * np.array([31,119,180], dtype=np.uint8)

#for i in range(len(quart)):
#    for j in range(len(quart[i])):
#        h = len(quart) - i
#        x = np.sqrt(h * h + j * j)
#        if(rayon >= x):
#            #print i,j
#            quart[i,j] = orange
x = np.linspace(-199.5, 199.5, 200)       
y = np.linspace(-199.5, 199.5, 200)    

X, Y = np.meshgrid(x,y)
print(X[0],X[1])

quart[rayon >= np.sqrt(X * X + Y * Y)] = orange


#quart = collerHorizontal(flipHorizontal(quart),quart)
#quart = collerVertical(quart,flipVertical(quart))
plt.imshow(quart)
plt.show()
