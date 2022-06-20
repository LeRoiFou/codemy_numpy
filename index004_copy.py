"""
Cours : Numpy Array Copy Vs View
Lien : https://www.youtube.com/watch?v=yAjzj2eShXU

Distinction entre l'instruction view() et copy() avec la modification d'un composant :
-> view() : le composant des deux arrays est modifié (dépendance de l'array original et de l'array copié)
-> copy() : le composant modifié dans l'array concerné ne se modifie pas dans l'autre array (indépendance entre l'array original et l'array modifié)

Éditeur : Laurent Reynaud
Date : 20-06-22
"""

import numpy as np

np1 = np.array([0,1,2,3,4,5])

# # Create a view()
# np2 = np1.view()

# print(f'Original NP1 {np1}')
# print(f'Original NP1 {np2}')

# np1[0] = 41

# print(f'Changed NP1 {np1}')
# print(f'Original NP1 {np2}') # composant 0 modifié également

# Create a copy()
np2 = np1.copy()

print(f'Original NP1 {np1}')
print(f'Original NP1 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP1 {np2}') # composant 0 non modifié cette fois-ci
