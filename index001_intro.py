"""
Cours : Intro To Numpy - Numpy For Machine Learning 1
Lien : https://www.youtube.com/watch?v=gnKbAAVUzro

Diverses instructions avec le package numpy

Éditeur : Laurent Reynaud
Date : 08-06-22
"""

import numpy as np

# Recours aux listes 'classiques'
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
list2 = ["John Elder", 41, list1, True]

# Recours à numpy
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

# Nombre de composants dans l'array
print(np1.shape)

# Liste de 1 à 10 en recourant à l'instruction 'arange'
np2 = np.arange(10)
print(np2)

# Liste de 0 à 10 par pas de 2
np3 = np.arange(0, 10, 2)
print(np3)

# Nombre de composant avec une valeur de 0
np4 = np.zeros(10)
print(np4)

# Liste à 2 dimensions comprenant 10 composants de valeur 0
np5 = np.zeros((2, 10))
print(np5)

# Liste de 10 composants avec une valeur de 6
np6 = np.full((10), 6)
print(np6)

# Liste à 2 dimensions avec 10 composants de chaque avec une valeur de 6
np7 = np.full((2, 10), 6)
print(np7)

# Conversion d'une liste en array
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

# Accès à un n° de composant
print(np8[2])
