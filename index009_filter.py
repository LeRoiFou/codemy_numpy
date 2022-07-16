"""
Cours : How To Filter Numpy Arrays
Lien : https://www.youtube.com/watch?v=gBd5cg5ELN0

Filtres effectués sur les arrays selon != méthodes

Éditeur : Laurent Reynaud
Date : 16-07-2022
"""

import numpy as np

# Filtering Numpy Arrays with Boolean Index Lists
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Method 1
# x = [True, True, False, False, False, False, False, False, False, False]
# print(np1[x])

# Method 2
# filtered = []
# for thing in np1:
#     if thing % 2 == 0:
#         filtered.append(True)
#     else:
#         filtered.append(False)
# print(filtered)
# print(np1[filtered])

# Method 3
filtered = np1 % 2 == 0
print(filtered)
print(np1[filtered])
