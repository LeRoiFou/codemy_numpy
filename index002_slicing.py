"""
Cours : Slicing Numpy Arrays - Numpy For Machine Learning 2
Lien : https://www.youtube.com/watch?v=PbKOrSottRQ

Dans ce cours on apprend à récupérer des "tranches" d'un array

Éditeur : Laurent Reynaud
Date : 14-06-22
"""

import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5
print(np1[1:5])

# Return from something till the end of the array ?
# 4 -> 9
print(np1[3:])

# Return negative slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5])
print(np1[1:5:2])

# Steps on the entire array
print(np1[::2])
print(np1[::3])

# Slice a 2-d array
np2 = np.array([
    [1,2,3,4,5], 
    [6,7,8,9,10]])

# Pull out a single item : 8
print(np2[1,2])

# Slice a 2-d array
print(np2[0:1, 1:3])

# Slice from both rows
print(np2[0:2, 1:3])
