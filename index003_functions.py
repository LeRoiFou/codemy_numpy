"""
Cours : Numpy Universal Functions
Lien : https://www.youtube.com/watch?v=4LIAHVXnpbY

Dans ce programme on apprend les méthodes rattachées au package numpy
Lien pour les fonctions : 
https://numpy.org/doc/stable/reference/ufuncs.html

Il semblerait que ce package a énormément de fonctions 
par rapport à Pandas...

Éditeur : Laurent Reynaud
Date : 16-06-22
"""

import numpy as np

np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])

# Square route of each element
# print(np.sqrt(np1))

# Absolute Value
print(np.absolute(np1))

# Exponentials
print(np.exp(np1))

# Min/Max
print(np.min(np1))
print(np.max(np1))

# Sign positive or negative
print(np.sign(np1))

# Trig sin cos log
# print(np.sin(np1))
# print(np.log(np1))
print(np.cos(np1))

#