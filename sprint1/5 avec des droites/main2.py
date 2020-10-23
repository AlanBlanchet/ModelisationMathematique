import numpy as np
import matplotlib.pyplot as plt

width = 300
height = 200

bleu = np.ones(3, dtype=np.int64) * [0, 17, 116]
jaune = np.ones(3, dtype=np.int64) * [254, 205, 36]
rouge = np.ones(3, dtype=np.int64) * [210, 38, 46]
blanc = np.ones(3, dtype=np.int64) * [0, 0, 0]
vert = np.ones(3, dtype=np.int64) * [0, 122, 51]

X, Y = np.meshgrid(np.arange(width, dtype=np.int64),
                   np.arange(height, dtype=np.int64),
                   indexing='ij')

seychelles = np.ones((height, width, 3), dtype = np.uint8) * 255


seychelles = seychelles[X < Y,:,:] = bleu


plt.imshow(seychelles)
plt.show()