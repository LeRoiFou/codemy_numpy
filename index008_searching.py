"""
Cours : Searching Numpy Arrays The Easy Way
Lien : https://www.youtube.com/watch?v=TE2BVmeVhJw

Recherche de composants dans l'array avec l'instruction where()

Éditeur : Laurent Reynaud
Date : 12-07-2022
"""

import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])

x = np.where(np1 == 3)
print(x)
print(x[0])
print(np1[x[0]])

# Return even times (impaires)
y = np.where(np1 % 2 == 0)
print(y[0])

# Return odd times (paires)
z = np.where(np1 % 2 == 1)
print(z[0])
